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
time.sleep(2)

# Obtain Data

driver.find_element(By.CLASS_NAME,"e6E1Yd").click()
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="liveresults-sports-immersive__team-fullpage"]/div/div[1]/div[2]/div/ol/li[3]').click()
time.sleep(10)





# Crear archivo Excel
planilha = openpyxl.Workbook()
partidos = planilha['Sheet']
partidos.title = 'Champions'
partidos['A1'] = 'equipo'
partidos['B1'] = 'pj'

planilha.save("championsleage.xlsx")
    