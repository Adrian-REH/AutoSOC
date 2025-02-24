import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.conf import settings


def send_email(body, subject):
	# Configuración
	smtp_server = "smtp.gmail.com"
	smtp_port = 587
	sender_email = settings.USER_EMAIL  # Reemplaza con tu correo
	receiver_email = settings.USER_EMAIL # Reemplaza con tu correo (puedes poner otro)
	password = settings.PASS_APP_EMAIL  # Reemplaza con tu contraseña o contraseña de aplicación

	msg = MIMEMultipart()
	msg['From'] = sender_email
	msg['To'] = receiver_email
	msg['Subject'] = subject
 
	msg.attach(MIMEText(body, 'plain'))

	try:
		server = smtplib.SMTP(smtp_server, smtp_port)
		server.starttls()  # Inicia el cifrado
		server.login(sender_email, password)  # Inicia sesión en el servidor
		text = msg.as_string()  # Convierte el mensaje a formato string
		server.sendmail(sender_email, receiver_email, text)  # Envía el correo
		print("Correo enviado exitosamente")
	except Exception as e:
		print(f"Error al enviar correo: {e}")
	finally:
		server.quit()  # Cierra la conexión
