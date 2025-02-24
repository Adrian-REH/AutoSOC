from django.urls import path
from .payment import procesar_pago

urlpatterns = [
    path("procesar-pago/", procesar_pago),
]
