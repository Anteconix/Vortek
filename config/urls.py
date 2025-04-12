from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from vortek.views import NotiticaViewSet, ComentarioViewSet, CriptoativoViewSet

router = DefaultRouter()
router.register(r"noticias", NotiticaViewSet)
router.register(r"criptoativos", ComentarioViewSet)
router.register(r"criptoativos", CriptoativoViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]