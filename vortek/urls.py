from django.urls import path
from .views import (
    CustomPasswordResetView,
    CustomPasswordResetConfirmView,
    preco_binance,
    mercado_binance,   # novo
)

urlpatterns = [
    path('reset_password/', CustomPasswordResetView.as_view(), name='reset_password'),
    path('reset_password_confirm/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),

    # endpoints da Binance via backend
    path('preco/<str:sigla>/', preco_binance, name='preco_binance'),
    path('mercado/', mercado_binance, name='mercado_binance'),
]
