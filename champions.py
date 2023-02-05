from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path=r'.\chomedriver.exe')

# Navigate to
driver.get("https://www.google.com.br")
inputElement = driver.find_element(By.CLASS_NAME, "gLFyf")
time.sleep(4)
inputElement.send_keys('resultados de champios leage'+ Keys.ENTER)
time.sleep(20)

