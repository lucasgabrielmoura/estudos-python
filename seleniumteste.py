import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Inicializa o driver do navegador (no exemplo, estamos utilizando o Chrome)
driver = webdriver.Edge()

# Navega até uma página da web
driver.get("https://www.youtube.com/")

# Interage com elementos da página
elemento = driver.find_element(By.XPATH,'//input[@id="search"]')
elemento2 = driver.find_element(By.XPATH,'//button[@id="search-icon-legacy"]')

time.sleep(2)
elemento.send_keys("Ruud")
elemento2.click()

time.sleep(2)
# Fecha o navegador
driver.quit()