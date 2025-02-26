from rest_framework.response import Response
from rest_framework.decorators import api_view
from .handle_email import send_email
from user_sessions.services import save_one_session
import requests
from django.conf import settings
import os
import pika
import json

def process_webdriver_alert_and_notify(request):
	ips = request.META.get('HTTP_X_FORWARDED_FOR', '').split(',') if request.META.get('HTTP_X_FORWARDED_FOR') else [request.META.get('REMOTE_ADDR')]

	# Procesar cada IP
	for ip in ips:
		session_processed = save_one_session(request.data, ip)
		if session_processed is None:
			return {"error": "Error processing session"}
		
		# Obtener los datos relevantes de la sesión procesada
		alert_count = session_processed.get("alert_count")
		session_data = session_processed.get("session_data", {})
		is_blocked = session_data.get("is_blocked")
		session_ip = session_data.get("ip")

		# Si es necesario trabajar con request.data, puedes hacerlo de la siguiente manera
		data = request.data.copy()  # Si es necesario modificar 'data' sin afectar el original

		data["security_level"] = "high"
		data["alert_type"] = "WebDriver detection"
		subject = f"""AutoSoc - IP: {ip}, Alert: N° - {alert_count} Webdriver detection, level: high """
		if is_blocked:
			subject = f"""AutoSoc - IP: {ip} ¡Is Blocked!, Alert: Webdriver detection, level: high """
			print(subject)
			for ip in ips:
				rabbitmq_send_ip(ip.strip(), True)

		body = f"""
		Se ha detectado un nuevo evento con la siguiente información:

		📍 Dirección IP: {request.data.get('ip')}
		🖥️ User-Agent: {request.data.get('user_agent','Desconocido')}
		🌍 Idioma: {request.data.get('language','Desconocido')}
		💻 Plataforma: {request.data.get('platform','Desconocido')}
		📏 Resolución de pantalla: {request.data.get('screen', {}).get('height', 'N/A')} x {request.data.get('screen', {}).get('width', 'N/A')}
		🕒 Timestamp: {request.data.get('timestamp', 'Desconocido')}

		🔒 Nivel de seguridad: high
		⚠️ Tipo de alerta: Webdriver detection"""

		send_email(body, subject)



def enviar_ip_bloqueada(channel,ip):
	message = {'ip': ip}

	channel.basic_publish(exchange='',
						routing_key='block_ip_queue',
						body=json.dumps(message))

	print(f"IP {ip} enviada para ser bloqueada.")

def rabbitmq_send_ip(ip, is_blocked):
	connection = pika.BlockingConnection(pika.ConnectionParameters(host=settings.HOST_RABBITMQ))
	channel = connection.channel()

	channel.queue_declare(queue='handle_ip_queue')
	message = {'is_blocked': is_blocked, 'ip': ip}

	channel.basic_publish(exchange='',
						routing_key='handle_ip_queue',
						body=json.dumps(message))

	print(f"IP {ip} enviada para ser bloqueada.")
	connection.close()

