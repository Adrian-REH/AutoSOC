from selenium import webdriver
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from handle_process import compile_exe, execute_process_top, exit_process, prepare_exe_process
import argparse


def init_selenium_ops(url):
	chrome_process = prepare_exe_process()
	if not chrome_process:
		print("No se pudo preparar el proceso Chrome.")
		return None, None
	options = webdriver.ChromeOptions()
	options.debugger_address = "127.0.0.1:9222"
	try:
		driver = webdriver.Chrome(
			service=Service("C:/SeleniumDrivers/chromedriver.exe"),  # Ruta del chromedriver
			options=options
		)
		driver.get(url)
		print("Conexión a Chrome exitosa.")
		return driver, chrome_process
	except Exception as e:
		print(f"Error al conectar Selenium a Chrome: {str(e)}")
		chrome_process.terminate()
		chrome_process.wait()
		return None, None


def main():
	parser = argparse.ArgumentParser(description="Ejemplo de manejo de argumentos en Python")

	parser.add_argument("url", type=str, help="Url para testear")
	args = parser.parse_args()

	time.sleep(4)
	driver, chrome_process = init_selenium_ops(args.url)
	if driver and chrome_process:
		time.sleep(4)
		driver.quit()
		chrome_process.terminate()
		chrome_process.wait()


# Ejecutar el programa principal
if __name__ == "__main__":
	main()

