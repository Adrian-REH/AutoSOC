from selenium import webdriver
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

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


 
# Ejecutar el programa principal
if __name__ == "__main__":
	url="https://store.local.com/"
	time.sleep(4)
	driver = init_selenium(url)
	time.sleep(4)
	driver.quit()

