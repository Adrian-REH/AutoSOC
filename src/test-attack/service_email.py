import smtplib
import os
import imaplib
import imapclient

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import imaplib
import email
import time
import os
from win10toast import ToastNotifier
from email.header import decode_header

from plyer import notification
IMAP_SERVER = "imap.gmail.com"  # Cambia esto según tu proveedor
EMAIL_ACCOUNT = os.getenv("USER_EMAIL")
EMAIL_PASSWORD = os.getenv("PASS_APP_EMAIL")

def send_email(subject, body):
	# Configuración
	smtp_server = "smtp.gmail.com"
	smtp_port = 587
	sender_email = os.getenv("USER_EMAIL")  # Reemplaza con tu correo
	receiver_email = os.getenv("USER_EMAIL") # Reemplaza con tu correo (puedes poner otro)
	password = os.getenv("PASS_APP_EMAIL")  # Reemplaza con tu contraseña o contraseña de aplicación

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


def fetch_last_emails(mail, ultimo_id):
    try:
        print(f" ultimo id: {ultimo_id}")

        status, mensajes = mail.select("INBOX")
        N = 1
        messages = int(mensajes[0])
        nuevos = []
        for i in range(messages, messages - N, -1):
            if i > ultimo_id:
                res, msg = mail.fetch(str(i), "(RFC822)")
                for response in msg:
                    if isinstance(response, tuple):
                        msg = email.message_from_bytes(response[1])

                        subject, encoding = decode_header(msg["Subject"])[0]
                        
                        if isinstance(subject, bytes):
                            subject = subject.decode(encoding or "utf-8")
                        msg_from, encoding = decode_header(msg.get("From"))[0]
                        if isinstance(msg_from, bytes):
                            msg_from = msg_from.decode(encoding or "utf-8")
                        body = ""
                        if msg.is_multipart():
                            # iterate over email parts
                            for part in msg.walk():
                                # extract content type of email
                                content_type = part.get_content_type()
                                content_disposition = str(part.get("Content-Disposition"))
                                try:
                                    body = part.get_payload(decode=True).decode()
                                except:
                                    pass
                        else:
                            content_type = msg.get_content_type()
                            # get the email body
                            body = msg.get_payload(decode=True).decode()
                            if content_type == "text/plain":
                                print("")
                        nuevos.append((i, { "msg_from" :msg_from, "subject":subject, "body":body}))
        return nuevos
    except Exception as e:
        print("Error:", e)
        return []

def show_notification(title, message):
    title = title[:55] + "..." 
    message = message[:240] + "..."
    notification.notify(
        title=title,
        message=message,
        app_icon="gmail.ico",  # Solo admite .ico
        timeout=3
    )

def notify_last_email():
    ultimo_id = 0  # Inicialmente ningún correo procesado
    while True:
        mail = imaplib.IMAP4_SSL(IMAP_SERVER)
        mail.login(EMAIL_ACCOUNT, EMAIL_PASSWORD)
        mail.select("inbox")
        nuevos = fetch_last_emails(mail, ultimo_id)
        for email_id, data  in nuevos:
            try:
                show_notification(data['subject'], data['body'])
            except Exception as e:
                print(f"Error:")

            ultimo_id = max(ultimo_id, email_id)  # Actualizar el último ID
        mail.logout()
        time.sleep(3)  # Revisar cada 60 segundos


if __name__ == "__main__":
    notify_last_email()
