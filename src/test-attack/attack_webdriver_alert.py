from selenium import webdriver
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import argparse
from colorama import Fore, Style, init

def init_selenium():
	print(f"{Fore.GREEN}[INFO] Inicializando Selenium con URL: {Style.RESET_ALL}")
	try:
		driver = webdriver.Chrome(
			service=Service("C:/SeleniumDrivers/chromedriver.exe"),
		)
		return driver
	except Exception as e:
		print(f"Error al conectar Selenium a Chrome: {str(e)}")
		return None

def open_new_tab_and_close_previous(driver, new_url):
	print(f"{Fore.GREEN}[ACTION] Abriendo nueva pestaña y cerrando la anterior en: {Fore.YELLOW}{new_url}{Style.RESET_ALL}")

	driver.execute_script("window.open('');")

	driver.switch_to.window(driver.window_handles[-1])  # Cambia al último handle, que es la nueva pestaña

	driver.get(new_url)

	driver.switch_to.window(driver.window_handles[0])  # Vuelve a la pestaña anterior
	driver.close()  # Cierra la pestaña anterior

	driver.switch_to.window(driver.window_handles[-1])  # Asegura que seguimos en la nueva pestaña

def main():
	parser = argparse.ArgumentParser(description="Ejemplo de manejo de argumentos en Python")
	parser.add_argument("url", type=str, help="Url para testear")
	args = parser.parse_args()
	print(f"{Fore.GREEN}[START] Iniciando prueba con URL: {Fore.YELLOW}{args.url}{Style.RESET_ALL}")

	driver = init_selenium()
	for i in range(4):
		print(f"{Fore.GREEN}[STEP {i+1}/4] Esperando 5 segundos antes de abrir nueva pestaña...{Style.RESET_ALL}")
		time.sleep(4)
		open_new_tab_and_close_previous(driver, args.url)
		page_text = driver.page_source.lower()
		if "403 forbidden" in page_text or "access denied" in page_text:
			print("🚫 Página bloqueada: 403 Forbidden")
			if driver:
				print(f"{Fore.RED}[END] Cerrando el driver de Selenium en 3 segundos...{Style.RESET_ALL}")
				time.sleep(3)
				driver.quit()
			return
		elif "451 Unavailable For Legal Reasons" in page_text:
			print(f"{Fore.GREEN}[SUCCESS] Blocked for using webDriver.{Style.RESET_ALL}")
	print(f"{Fore.GREEN}[SUCCESS] Test: 403 Blocked for repeated WebDriver use, with 451 response for legal reasons.{Style.RESET_ALL}")

	if driver:
		print(f"{Fore.RED}[END] Cerrando el driver de Selenium en 5 segundos...{Style.RESET_ALL}")
		time.sleep(5)
		driver.quit()


if __name__ == "__main__":
	main()


