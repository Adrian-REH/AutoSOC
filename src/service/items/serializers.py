# src/service/items/serializers.py
from rest_framework import serializers
from .models import Item  # Asegúrate de que tienes el modelo Item definido

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name', 'price', 'stock']  # Puedes especificar los campos que quieres serializar
