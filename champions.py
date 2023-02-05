from selenium import webdriver
import time
import openpyxl
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options



# Libreria Chrome
driver = webdriver.Chrome(executable_path=r'.\chomedriver.exe')

# Navigate to
driver.get("https://www.google.com.br")
inputElement = driver.find_element(By.CLASS_NAME, "gLFyf")
time.sleep(4)
inputElement.send_keys('resultados de champios leage tabla'+ Keys.ENTER)
time.sleep(4)

# Obtain Data
button = driver.find_element(By.CLASS_NAME,"U0faLd CNf3nf OvQkSb LhCR5d")
button.click()
time.sleep(60)






