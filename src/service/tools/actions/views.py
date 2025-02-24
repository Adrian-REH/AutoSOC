from rest_framework.response import Response
from rest_framework.decorators import api_view
from .handle_email import send_email
import requests

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

    ip = request.data.get('ip')
    userAgent = request.data.get('userAgent','Desconocido')
    language = request.data.get('language','Desconocido')
    platform = request.data.get('platform','Desconocido')
    height = request.data.get('screen', {}).get('height', 'N/A')
    width = request.data.get('screen', {}).get('width', 'N/A')
    timestamp = request.data.get('timestamp', 'Desconocido')
    data = request.data.copy()
    data["security_level"] = "high"
    data["alert_type"] = "WebDriver detection"
    body = f"""
    Se ha detectado un nuevo evento con la siguiente información:

    📍 Dirección IP: {ip}
    🖥️ User-Agent: {userAgent}
    🌍 Idioma: {language}
    💻 Plataforma: {platform}
    📏 Resolución de pantalla: {height} x {width}
    🕒 Timestamp: {timestamp}

    🔒 Nivel de seguridad: high
    ⚠️ Tipo de alerta: Webdriver detection"""
    subject = f"""AutoSoc - IP: {ip}, Alert: Webdriver detection, level: high """
    send_email(body, subject)
    return Response({"message": f"Se ejecuto PowerAction Alert Use WebDriver IP: {ip} Timestamp: {timestamp}"})

@api_view(['POST'])
def csp_alert(request):
    ip = request.data.get('ip')
    # Aquí iría la lógica para hacer seguimiento a la IP
    return Response({"message": f"Se ejecuto PowerAction Alert non-compliance csp IP: {ip}"})
