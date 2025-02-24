from selenium import webdriver
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import argparse

def init_selenium(url):
	try:
		driver = webdriver.Chrome(
			service=Service("C:/SeleniumDrivers/chromedriver.exe"),
		)
		driver.get(url)
		print("Conexión a Chrome exitosa.")
		return driver
	except Exception as e:
		print(f"Error al conectar Selenium a Chrome: {str(e)}")
		return None


def main():
	parser = argparse.ArgumentParser(description="Ejemplo de manejo de argumentos en Python")

	parser.add_argument("url", type=str, help="Url para testear")
	args = parser.parse_args()

	time.sleep(4)
	driver = init_selenium(args.url)
	if driver:
		time.sleep(4)
		driver.quit()


if __name__ == "__main__":
    main()


