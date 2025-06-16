from rest_framework.serializers import ModelSerializer, CharField, EmailField, ImageField
from vortek.models import Noticia, Comentario, Criptoativo, Aporte, Usuario

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
    criptoativo = CriptoativoSerializer(read_only=True)
    moeda = CharField(write_only=True, required=False)

    class Meta:
        model = Aporte
        fields = ['id', 'usuario', 'criptoativo', 'data_aporte', 'valor_aportado', 'quantidade', 'moeda']
        read_only_fields = ['usuario', 'criptoativo']

class UsuarioSerializer(ModelSerializer):
    email = EmailField()
    foto_perfil = ImageField(required=False, allow_null=True)

    class Meta:
        model = Usuario
        fields = ['id', 'nome_completo', 'email', 'foto_perfil']