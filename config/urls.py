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
    path("api/", include(router.urls)),
    path("api/user/", UserView.as_view()),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path('api/preco/<str:sigla>/', preco_binance),
    # Rotas para redefinição de senha
    path('api/reset_password/', CustomPasswordResetView.as_view(), name='custom_password_reset'),
    path('api/reset_password_confirm/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='custom_password_reset_confirm'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
