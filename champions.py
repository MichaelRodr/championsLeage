from selenium import webdriver
import time


driver = webdriver.Chrome(executable_path=r'.\chomedriver.exe')

driver.get("https://www.google.com")
inputElement =driver.find_element("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input").click()
time.sleep(4)

