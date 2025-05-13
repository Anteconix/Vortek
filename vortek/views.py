from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from vortek.models import Noticia, Comentario, Criptoativo, Aporte, Usuario
from vortek.serializers import (
    NoticiaSerializer,
    ComentarioSerializer,
    CriptoativoSerializer,
    AporteSerializer,
    UsuarioSerializer
)

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

class UserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UsuarioSerializer(request.user)
        return Response(serializer.data)
