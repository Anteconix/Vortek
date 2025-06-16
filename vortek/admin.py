from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario, Noticia, Comentario, Criptoativo

@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    model = Usuario
    fieldsets = UserAdmin.fieldsets + (
        ('Informações adicionais', {'fields': ('nome_completo', 'foto_perfil')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Informações adicionais', {'fields': ('nome_completo', 'foto_perfil')}),
    )
    list_display = ('email', 'username', 'nome_completo', 'is_staff')
    search_fields = ('email', 'nome_completo', 'username')

admin.site.register(Noticia)
admin.site.register(Comentario)
admin.site.register(Criptoativo)
