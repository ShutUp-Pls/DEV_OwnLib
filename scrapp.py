# scrapp.py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import tkinter as tk
from tkinter import messagebox


class ScrapTool:
    def __init__(self):
        self.__driver = None

    def __init_driver(self):
        """Inicializa el driver de Selenium en modo headless."""
        chrome_options = Options()
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        self.__driver = webdriver.Chrome(options=chrome_options)

    def __load_page(self, url):
        """Carga la página y espera a que termine la ejecución de JS."""
        self.__driver.get(url)

    def __find_element_by_xpath(self, xpath):
        """Busca el elemento usando XPath."""
        try:
            element = WebDriverWait(self.__driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            return element
        except:
            return None

    def doScrap(self, url, xpath):
        """Proceso principal de scrapping."""
        try:
            self.__init_driver()
            self.__load_page(url)
            element = self.__find_element_by_xpath(xpath)

            root = tk.Tk()
            root.withdraw()

            if element:
                messagebox.showinfo("Scrapping exitoso", f"Elemento encontrado: {element.text[:50]}...")
            else:
                messagebox.showerror("Error", "No se encontró el elemento con el XPath dado.")

        except Exception as e:
            root = tk.Tk()
            root.withdraw()
            messagebox.showerror("Error crítico", str(e))
        finally:
            if self.__driver:
                self.__driver.quit()


# Ejecución directa para pruebas
if __name__ == "__main__":
    url_test = "https://www.wikipedia.org/"
    xpath_test = '//*[@id="www-wikipedia-org"]/div[1]/div/h1/span'  # Ejemplo: título
    scraper = ScrapTool()
    scraper.doScrap(url_test, xpath_test)
