from rest_framework.response import Response
from rest_framework.decorators import api_view
from .handle_email import send_email
from user_sessions.services import save_one_session
import requests

def process_webdriver_alert_and_notify(request):
	session_processed = save_one_session(request)
	if session_processed is None:
		return {"error": "Error processing session"}

	alert_count = session_processed.get("alert_count")
	is_blocked = session_processed.get("is_blocked")
	data = request.data.copy()
	data["security_level"] = "high"
	data["alert_type"] = "WebDriver detection"
	body = f"""
	Se ha detectado un nuevo evento con la siguiente información:

	📍 Dirección IP: {request.data.get('ip')}
	🖥️ User-Agent: {request.data.get('user_agent','Desconocido')}
	🌍 Idioma: {request.data.get('language','Desconocido')}
	💻 Plataforma: {request.data.get('platform','Desconocido')}
	📏 Resolución de pantalla: {request.data.get('screen', {}).get('height', 'N/A')} x {request.data.get('screen', {}).get('width', 'N/A')}
	🕒 Timestamp: {request.data.get('timestamp', 'Desconocido')}

	🔒 Nivel de seguridad: high
	⚠️ Tipo de alerta: Webdriver detection, N°: {alert_count}"""
	subject = f"""AutoSoc - IP: {ip}, Alert: Webdriver detection, level: high """
	if is_blocked:
		subject = f"""AutoSoc - IP: {ip} ¡Is Blocked!, Alert: Webdriver detection, level: high """
	send_email(body, subject)