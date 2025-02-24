from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def health_check(request):
    return Response({"message": f"ON"})


@api_view(['POST'])
def block_ip(request):
    ip = request.data.get('ip')
    # Aquí iría la lógica para bloquear la IP
    return Response({"message": f"IP {ip} bloqueada exitosamente"})

@api_view(['POST'])
def follow_ip(request):
    ip = request.data.get('ip')
    # Aquí iría la lógica para hacer seguimiento a la IP
    return Response({"message": f"Siguiendo actividad de IP: {ip}"})

@api_view(['POST'])
def webdriver_alert(request):
    ip = request.data.get('ip')
    # Aquí iría la lógica para hacer seguimiento a la IP
    return Response({"message": f"Se ejecuto PowerAction Alert Use WebDriver IP: {ip}"})

@api_view(['POST'])
def csp_alert(request):
    ip = request.data.get('ip')
    # Aquí iría la lógica para hacer seguimiento a la IP
    return Response({"message": f"Se ejecuto PowerAction Alert non-compliance csp IP: {ip}"})
