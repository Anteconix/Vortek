from django.db import models

class Noticia(models.Model):
    titulo_noticia = models.CharField(max_length=100)
    conteudo_noticia = models.TextField()
    ##fazer a imagem funfar 😢
    def __str__(self):
        return self.titulo_noticia

class Comentario(models.Model):
##    nome_usuario = models.ForeignKey(
##        User,
##        on_delete=models.CASCADE,
##        related_name="comentarios",
##    )

##      tem que ver isso também ☝😭
    conteudo_comentario = models.TextField()
##    def __str__(self):
##        return self.nome_usuario

class Criptoativo(models.Model):
    cripto_sigla = models.CharField(max_length=10)
    Criptoativo = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=3)
    def __str__(self):
            return self.cripto_sigla

class Criptoativo_adq(models.Model):
    cripto_sigla = models.ForeignKey(Criptoativo, on_delete=models.CASCADE, related_name="cripto_siglas")
    criptoativo = models.ForeignKey(Criptoativo, on_delete=models.CASCADE, related_name="criptoativos")
    quant_adq = models.DecimalField(max_digits=10, decimal_places=3)
    valor = models.ForeignKey(Criptoativo, on_delete=models.CASCADE, related_name="valors")
    def __str__(self):
        return self.cripto_sigla