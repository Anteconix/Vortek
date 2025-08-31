import requests
from rest_framework.decorators import api_view, permission_classes
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.parsers import MultiPartParser, FormParser
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from vortek.models import Noticia, Comentario, Criptoativo, Aporte, Usuario
from vortek.serializers import (
    NoticiaSerializer,
    ComentarioSerializer,
    CriptoativoSerializer,
    AporteSerializer,
    UsuarioSerializer
)

from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from django.conf import settings

# ===============================
# API de preço (proxy da Binance)
# ===============================
@api_view(['GET'])
@permission_classes([AllowAny])
def preco_binance(request, sigla):
    """ Consulta o preço atual de uma cripto em BRL via Binance """
    try:
        symbol = f"{sigla.upper()}BRL"
        url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
        r = requests.get(url, timeout=5)
        if r.status_code == 200:
            data = r.json()
            return Response({"preco": data.get("price")})
        return Response({"erro": "Preço não encontrado na Binance"}, status=404)
    except Exception as e:
        return Response({"erro": f"Erro ao consultar Binance: {e}"}, status=500)

# ===============================
# API de mercado (lista 24h Binance)
# ===============================
@api_view(['GET'])
@permission_classes([AllowAny])
def mercado_binance(request):
    """ Retorna os tickers 24h da Binance (proxy) """
    try:
        url = "https://api.binance.com/api/v3/ticker/24hr"
        r = requests.get(url, timeout=5)
        if r.status_code == 200:
            return Response(r.json())
        return Response({"erro": "Não foi possível obter dados da Binance"}, status=404)
    except Exception as e:
        return Response({"erro": f"Erro ao consultar Binance: {e}"}, status=500)


User = get_user_model()

# ===============================
# CRUDs
# ===============================
class NotiticaViewSet(ModelViewSet):
    queryset = Noticia.objects.all()
    serializer_class = NoticiaSerializer

class ComentarioViewSet(ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer
    permission_classes = [IsAuthenticated]

class CriptoativoViewSet(ModelViewSet):
    queryset = Criptoativo.objects.all()
    serializer_class = CriptoativoSerializer

class AporteViewSet(ModelViewSet):
    queryset = Aporte.objects.all()
    serializer_class = AporteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Aporte.objects.filter(usuario=self.request.user)

    def perform_create(self, serializer):
        cripto_id = self.request.data.get('criptoativo')
        criptoativo = Criptoativo.objects.get(id=cripto_id)
        serializer.save(usuario=self.request.user, criptoativo=criptoativo)

class UserView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request):
        serializer = UsuarioSerializer(request.user)
        return Response(serializer.data)

    def put(self, request):
        serializer = UsuarioSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ===============================
# Fluxo de reset de senha
# ===============================
def _get_frontend_url() -> str:
    return getattr(settings, "FRONTEND_URL", "http://localhost:5173").rstrip("/")

@method_decorator(csrf_exempt, name='dispatch')
class CustomPasswordResetView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = (request.data.get('email') or "").strip().lower()
        if not email:
            return Response({'erro': 'Email é obrigatório.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'mensagem': 'Se o e-mail existir, enviaremos instruções de redefinição.'}, status=status.HTTP_200_OK)

        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = default_token_generator.make_token(user)

        frontend_url = _get_frontend_url()
        reset_link = f"{frontend_url}/login?uid={uid}&token={token}"

        nome = getattr(user, "nome_completo", None) or getattr(user, "first_name", "") or ""
        subject = "Redefinição de senha"
        message = (
            f"Olá {nome},\n\n"
            f"Você solicitou a redefinição da sua senha.\n"
            f"Acesse o link abaixo para continuar:\n\n{reset_link}\n\n"
            f"Se você não solicitou, ignore este e-mail."
        )

        from_email = getattr(settings, "DEFAULT_FROM_EMAIL", getattr(settings, "EMAIL_HOST_USER", None)) or "no-reply@localhost"

        send_mail(subject, message, from_email, [email], fail_silently=False)
        return Response({'mensagem': 'Se o e-mail existir, enviaremos instruções de redefinição.'}, status=status.HTTP_200_OK)


@method_decorator(csrf_exempt, name='dispatch')
class CustomPasswordResetConfirmView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, uidb64, token):
        nova_senha = request.data.get('nova_senha')
        if not nova_senha:
            return Response({'erro': 'Nova senha é obrigatória.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (User.DoesNotExist, ValueError, TypeError, OverflowError):
            return Response({'erro': 'Link inválido ou expirado.'}, status=status.HTTP_400_BAD_REQUEST)

        if not default_token_generator.check_token(user, token):
            return Response({'erro': 'Token inválido.'}, status=status.HTTP_400_BAD_REQUEST)

        user.set_password(nova_senha)
        user.save()
        return Response({'mensagem': 'Senha redefinida com sucesso.'}, status=status.HTTP_200_OK)


class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        old_password = request.data.get("old_password")
        new_password = request.data.get("new_password")

        if not old_password or not new_password:
            return Response({"detail": "Campos obrigatórios não enviados."}, status=status.HTTP_400_BAD_REQUEST)

        if not user.check_password(old_password):
            return Response({"detail": "Senha anterior incorreta."}, status=status.HTTP_400_BAD_REQUEST)

        user.set_password(new_password)
        user.save()
        return Response({"detail": "Senha alterada com sucesso."}, status=status.HTTP_200_OK)
