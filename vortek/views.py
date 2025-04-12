from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from vortek.models import Noticia, Comentario, Criptoativo
from vortek.serializers import NoticiaSerializer, ComentarioSerializer, CriptoativoSerializer

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