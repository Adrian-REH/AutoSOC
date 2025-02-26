import pika
import requests
import time
import os
import json
import subprocess

NGINX_BLOCKLIST = "/etc/nginx/blocked_ips.conf"
if not os.path.exists(NGINX_BLOCKLIST):
	open(NGINX_BLOCKLIST, "w").close()  # Crea el archivo vacío si no existe


def check_nginx_configuration():
	try:
		# Ejecutar 'nginx -t' para comprobar la configuración
		result = subprocess.run(['nginx', '-t'], capture_output=True, text=True)
		
		# Si el comando tiene un error, se lanza una excepción
		if result.returncode != 0:
			print(f"Error en la configuración de Nginx: {result.stderr}")
			return False
		print("Configuración de Nginx válida.")
		return True
	except Exception as e:
		print(f"Error al verificar la configuración de Nginx: {e}")
		return False


def reload_nginx():
	try:
		# Ejecutar 'nginx -s reload' para recargar la configuración
		result = subprocess.run(['nginx', '-s', 'reload'], capture_output=True, text=True)
		
		# Si hay algún error, se lanza una excepción
		if result.returncode != 0:
			print(f"Error al recargar Nginx: {result.stderr}")
		else:
			print("Nginx recargado correctamente.")
	except Exception as e:
		print(f"Error al recargar Nginx: {e}")


def reload_conf_nginx(ip_bloqueada):
    # Leer las IPs existentes
    try:
        with open(NGINX_BLOCKLIST, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        lines = []

    # Convertir a conjunto para evitar duplicados
    ips_existentes = {line.strip() for line in lines}

    # Agregar la nueva IP solo si no existe
    if f"deny {ip_bloqueada};" not in ips_existentes:
        ips_existentes.add(f"deny {ip_bloqueada};")

    # Escribir de nuevo sin duplicados
    with open(NGINX_BLOCKLIST, 'w') as f:
        f.write("\n".join(ips_existentes) + "\n")

    # Recargar Nginx
    reload_nginx()
    print(f"IP {ip_bloqueada} bloqueada y Nginx recargado.")

def remove_ip_from_nginx(ip):
	"""Elimina una IP bloqueada del archivo y recarga Nginx"""
	try:
		with open(NGINX_BLOCKLIST, 'r') as f:
			lines = f.readlines()

		# Filtrar todas las líneas excepto la que contiene la IP
		new_lines = [line for line in lines if f"deny {ip};" not in line]

		with open(NGINX_BLOCKLIST, 'w') as f:
			f.writelines(new_lines)

		# Recargar Nginx
		reload_nginx()
		print(f"IP {ip} eliminada y Nginx recargado.")
	except FileNotFoundError:
		print("El archivo de bloqueos no existe.")

def callback(ch, method, properties, body):
	print("Mensaje recibido:", body)
	try:
		message = json.loads(body)
		ip = message['ip']
		is_blocked = message['is_blocked']
		if is_blocked:
			reload_conf_nginx(ip)
		else:
			remove_ip_from_nginx(ip)
		ch.basic_ack(delivery_tag=method.delivery_tag)
	except Exception as e:
		print(f"Error processing message: {e}")
		ch.basic_ack(delivery_tag=method.delivery_tag, requeue=True)



def main():
	while True:
		try:
			connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
			channel = connection.channel()
			channel.queue_declare(queue='handle_ip_queue')
			channel.basic_consume(queue='handle_ip_queue', on_message_callback=callback, auto_ack=False)
			print('Esperando block_ip_queue. Para salir presiona CTRL+C')
			channel.start_consuming()
		except pika.exceptions.AMQPConnectionError:
			print("No se pudo conectar a RabbitMQ. Reintentando en 5 segundos...")
			time.sleep(5)

if __name__ == '__main__':
	main()
