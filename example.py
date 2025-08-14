from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Opciones (modo headless si quieres)
options = Options()
# options.add_argument("--headless")  # si quieres que no se vea

# Inicializar el driver
driver = webdriver.Chrome(options=options)

# 1. Navegar a la URL
driver.get("https://es.wikipedia.org/wiki/Wikipedia:Portada")

# 2. Esperar a que aparezca un elemento (por ejemplo un h1)
wait = WebDriverWait(driver, 10)
titulo = wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))

# 3. Extraer texto
print(titulo.text)

# 4. Cerrar navegador
driver.quit()
