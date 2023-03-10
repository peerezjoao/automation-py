from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from datetime import date
import pandas as pd
import time
import os

df = pd.read_excel("C:\\Users\\peere\\automation-py\\stocks_automation\\templates\\FundsExplorer.xlsx")
print(df)

chromedrive = '.\stocks_automation\chromedriver.exe'

driver = webdriver.Chrome(chromedrive)
driver.get('https://www.fundsexplorer.com.br/')
driver.maximize_window()

wait = WebDriverWait(driver, timeout=15.0)

# find popup
try: 
    wait.until(EC.visibility_of_element_located((By.ID, 'popup-close-button')))
    driver.find_element(By.XPATH, '/html/body/div[2]/div/div[7]').click()
    print('Popup localizada com sucesso.')
except:
    print('Popup não localizada, prosseguindo com a automação.')
    
# search -- Reit 
driver.find_element(By.XPATH, '//*[@id="search-desktop"]').click()
time.sleep(2)
driver.find_element(By.CLASS_NAME, "select2-search__field").click()
driver.find_element(By.CLASS_NAME, "select2-search__field").send_keys('HGLG11')
driver.find_element(By.CLASS_NAME, "select2-search__field").send_keys(Keys.ENTER)

# find new popup
try:
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'close-button')))
    driver.find_element(By.CLASS_NAME, 'close-button').click()
except:
    print('Nova popup não foi localizada dessa vez.')


# webscraping 
print('Extraindo informações...')
lista_titulos = driver.find_elements(By.CLASS_NAME, 'indicator-title')
lista_elementos = driver.find_elements(By.CLASS_NAME, 'indicator-value')

for ti, el in zip(lista_titulos, lista_elementos):
    print(f'{ti.text}: {el.text}')
    
    df.loc[df['Fiis']=='HGLG11'].index
    
    
print('Verificando se existe algum relatório')
lista_tabelas = driver.find_elements(By.ID, "DataTables_Table_0")

print(date.today().strftime('%d/%m/%Y'))
for item, index in lista_tabelas:
    print(item.text)
    if (item.text.__contains__("Relatórios - ")):
        print(f'Relatório disponível para baixar: {item.text} \n' +
              'prerando para baixar relatório.')
        driver.find_element(By.CLASS_NAME, "bulletin-list_view")[index].click()
        driver.window_handles[1]
        wait.until(EC.visibility_of_any_elements_located((By.XPATH, '//*[@id="icon"]/iron-icon//svg')))
        
        
    if (item.text.__contains__("Fato Relevante")):
        print('Fato relevante detectado.')

time.sleep(10)
print('Automação executada com sucesso.')


