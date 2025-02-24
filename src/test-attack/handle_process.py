import subprocess
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

def exit_process(process):
	if process:
		process.terminate()
		process.wait()
		print("Successful Finished Process.")

# Paso 1: Compilar chrome_process.cpp
def compile_exe(compile_command = "c++ chrome_process.cpp -o chrome_process"):
	compile_command = compile_command.split(" ")
	try:
		process = subprocess.run(
			compile_command,  # Compilar y generar ejecutable "chrome_process"
			check=True,                         # Lanza excepción si hay error
			stdout=subprocess.PIPE,             # Captura la salida estándar
			stderr=subprocess.PIPE              # Captura los errores
		)
		print("Compilación exitosa:", process.stdout.decode())
		return True
	except subprocess.CalledProcessError as e:
		print("Error en la compilación:", e.stderr.decode())
		return False

# Paso 2: Ejecutar el chrome_process.exe
def execute_process(execute_command="./chrome_process"):
	execute_command = execute_command.split(" ")
	chrome_process = None
	try:
		chrome_process = subprocess.Popen(
			execute_command,                # Ejecutar el proceso compilado
			stdout=subprocess.PIPE,            # Capturar la salida estándar
			stderr=subprocess.PIPE             # Capturar la salida de error
		)
		print("Proceso iniciado correctamente. ")
		time.sleep(1)
		return chrome_process
	except Exception as e:
		print(f"Error al iniciar el proceso: {str(e)}")
		return None

def execute_process_top(execute_command="./chrome_process"):
	execute_command = execute_command.split(" ")
	try:
		process = subprocess.run(
			execute_command,  # Compilar y generar ejecutable "chrome_process"
			check=True,                         # Lanza excepción si hay error
			stdout=subprocess.PIPE,             # Captura la salida estándar
			stderr=subprocess.PIPE              # Captura los errores
		)
		print("Compilación exitosa:", process.stdout.decode())
		return True
	except subprocess.CalledProcessError as e:
		print("Error en la compilación:", e.stderr.decode())
		return False

def prepare_exe_process(compile_command = "c++ chrome_process.cpp -o chrome_process", execute_command = "./chrome_process"):
	if not compile_exe(compile_command):
		return None
	return execute_process(execute_command)