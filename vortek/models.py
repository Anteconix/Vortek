from django.db import models
from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser):
    nome_completo = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    foto_perfil = models.ImageField(upload_to='perfil/', null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'nome_completo']

    def __str__(self):
        return self.email

class Noticia(models.Model):
    titulo_noticia = models.CharField(max_length=100)
    conteudo_noticia = models.TextField()

    def __str__(self):
        return self.titulo_noticia

class Comentario(models.Model):
    conteudo_comentario = models.TextField()

class Criptoativo(models.Model):
    cripto_sigla = models.CharField(max_length=10)
    Criptoativo = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=3)

    def __str__(self):
        return self.cripto_sigla

class Aporte(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    criptoativo = models.ForeignKey(Criptoativo, on_delete=models.CASCADE)
    data_aporte = models.DateField()
    valor_aportado = models.DecimalField(max_digits=10, decimal_places=3)
    quantidade = models.DecimalField(max_digits=10, decimal_places=8)

    def __str__(self):
        return f"{self.usuario.email} - {self.criptoativo.cripto_sigla} - R$ {self.valor_aportado}"
