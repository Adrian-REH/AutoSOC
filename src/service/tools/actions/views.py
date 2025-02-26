from rest_framework.response import Response
from rest_framework.decorators import api_view
from .handle_email import send_email
from user_sessions.services import save_one_session
from .services import process_webdriver_alert_and_notify
import requests
from rest_framework import status

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
    """     url_power_automate = ''
    headers = {
        'Content-Type': 'application/json',
    }
    response = requests.post(url, json=data, headers=headers) """
    ip = request.data.get("ip")
    timestamp = request.data.get("timestamp")
    try:
        process_webdriver_alert_and_notify(request)
    except Exception as e:
        print(f"Error: {str(e)}")
        return Response({"message": "Error"}, status=status.HTTP_400_BAD_REQUEST)
        

    return Response({"message": f"Se ejecuto PowerAction Alert Use WebDriver IP: {ip} Timestamp: {timestamp}"})

@api_view(['POST'])
def csp_alert(request):
    ip = request.data.get('ip')
    # Aquí iría la lógica para hacer seguimiento a la IP
    return Response({"message": f"Se ejecuto PowerAction Alert non-compliance csp IP: {ip}"})
