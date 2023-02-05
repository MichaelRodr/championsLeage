from selenium import webdriver
import time
from selenium.webdriver.common.keys import keys
from selenium.webdriver.common.by import by

driver = webdriver.Chrome(executable_path=r'.\chomedriver.exe')

driver.get("https://www.google.com")
driver.find_element("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input").click()
time.sleep(4)


