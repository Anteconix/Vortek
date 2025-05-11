from rest_framework.serializers import ModelSerializer

from vortek.models import Noticia, Comentario, Criptoativo, Aporte

class NoticiaSerializer(ModelSerializer):
    class Meta:
        model = Noticia
        fields = "__all__"

class ComentarioSerializer(ModelSerializer):
    class Meta:
        model = Comentario
        fields = "__all__"

class CriptoativoSerializer(ModelSerializer):
    class Meta:
        model = Criptoativo
        fields = ['id', 'cripto_sigla', 'Criptoativo', 'valor']


class AporteSerializer(ModelSerializer):
    class Meta:
        model = Aporte
        fields = '__all__'
