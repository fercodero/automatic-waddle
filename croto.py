from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
compra = input("ingrese lo que quiere comprar")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, executable_path="path/to/executable")
driver.get("https://www.historial.com.ar/ofertas;{}" .format(compra))