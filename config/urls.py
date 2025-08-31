from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter
from django.contrib.auth import views as auth_views

from vortek.views import (
    NotiticaViewSet,
    ComentarioViewSet,
    CriptoativoViewSet,
    AporteViewSet,
    UserView,
    CustomPasswordResetView,
    CustomPasswordResetConfirmView,
    preco_binance
)

router = DefaultRouter()
router.register(r"noticias", NotiticaViewSet)
router.register(r"comentarios", ComentarioViewSet)
router.register(r"criptoativos", CriptoativoViewSet)
router.register(r"aportes", AporteViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),

    # Rotas de ViewSets
    path("api/", include(router.urls)),

    # Rotas de API próprias do app (reset de senha, etc.)
    path("api/", include("vortek.urls")),  # <-- ADICIONADO

    # Usuário e JWT
    path("api/user/", UserView.as_view()),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    # Outros endpoints
    path('api/preco/<str:sigla>/', preco_binance),

    # === Aliases compatíveis com o frontend (Vue) ===
    # O Vue chama /password_reset/ com { "email": "..." }
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset_alias'),
    # O Vue chama /reset/<uidb64>/<token>/ com { "nova_senha": "..." }
    path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm_alias'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)