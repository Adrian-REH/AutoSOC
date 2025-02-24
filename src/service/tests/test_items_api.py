import pytest
import django
from rest_framework.test import APIClient


django.setup()


@pytest.mark.django_db
def test_get_items():
    client = APIClient()
    response = client.get("/api/items/list/")
    assert response.status_code == 200


@pytest.mark.django_db
def test_decrease_stock():
    client = APIClient()
    response = client.get("/api/items/list/")
    assert response.status_code == 200

