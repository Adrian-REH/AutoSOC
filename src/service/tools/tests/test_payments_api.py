import pytest
from rest_framework.test import APIClient
from django.conf import settings
import json


@pytest.mark.django_db
def test_process_payment():

    client = APIClient()
    
    headers = {"Content-Type": "application/json"}
    
    # Enviar el token al backend para procesar el pago
    response = client.post(
        "/api/payments/process-payment/", 
        {
        "amount": 100,
        "email": "adrianherrera.r.e@gmail.com",
        "token": "tok_visa"  # Cambiar 'token' a 'source'
    },
        format='json'
    )
    
    assert response.status_code == 200
    assert response.json()['success'] == True

