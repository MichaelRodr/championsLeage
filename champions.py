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



lista_equipos = []
lista_pj = []

for datos in range():
     item = 1
     for i in range(20):
                lista_equipos = driver.find_element(By.XPATH,
                    f'//*[@id="sports-app"]/div/div[3]/div[2]/div/div/div/div/div/div/div[2]/div/div[2]/div/table/tbody/tr[2]/td[3]/div/div/span')
                lista_equipos.append(lista_equipos[0].text)
                time.sleep(1)
                lista_pj = driver.find_elements(By.XPATH,
                    f'//*[@id="sports-app"]/div/div[3]/div[2]/div/div/div/div/div/div/div[2]/div/div[2]/div/table/tbody/tr[2]/td[4]')
                lista_pj.append(lista_pj[0].text)
                item += 1
                time.sleep(1)

# Crear archivo Excel
planilha = openpyxl.Workbook()
partidos = planilha['Sheet']
partidos.title = 'Champions'
partidos['A1'] = 'equipo'
partidos['B1'] = 'pj'

planilha.save("championsleage.xlsx")
    