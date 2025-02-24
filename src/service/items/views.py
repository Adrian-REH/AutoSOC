from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Item
from .serializers import ItemSerializer


@api_view(['GET'])
def list_items(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)


@api_view(['PUT'])
def decrease_stock(request):
    data = request.data  # Recibir datos del request (lista de items con id y stock)

    if not isinstance(data, list):  # Verificar que se recibe una lista
        return Response({"error": "Invalid data format, expected a list"}, status=400)

    updated_items = []  # Lista para almacenar los ítems actualizados

    for item_data in data:
        item_id = item_data.get("id")
        new_stock = item_data.get("stock")

        if item_id is None or new_stock is None:
            return Response({"error": "Missing 'id' or 'stock' in request"}, status=400)

        try:
            item = Item.objects.get(id=item_id)
            item.stock = max(0, item.stock - new_stock)
            item.save()
            updated_items.append(item)
        except Item.DoesNotExist:
            return Response({"error": f"Item with id {item_id} not found"}, status=404)
    serializer = ItemSerializer(updated_items, many=True)
    return Response(serializer.data, status=200)