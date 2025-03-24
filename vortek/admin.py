from django.contrib import admin

from .models import Noticia,Comentario,Criptoativo,Criptoativo_adq

admin.site.register(Noticia)
admin.site.register(Comentario)
admin.site.register(Criptoativo)
admin.site.register(Criptoativo_adq)