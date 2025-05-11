from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from rest_framework.routers import DefaultRouter

from vortek.views import NotiticaViewSet, ComentarioViewSet, CriptoativoViewSet, AporteViewSet

router = DefaultRouter()
router.register(r"noticias", NotiticaViewSet)   
router.register(r"comentarios", ComentarioViewSet)
router.register(r"criptoativos", CriptoativoViewSet)
router.register(r"aportes", AporteViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]