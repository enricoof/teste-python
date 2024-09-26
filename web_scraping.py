from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

driver = webdriver.Chrome()

driver.get('https://ge.globo.com/futebol/brasileirao-serie-a/')

time.sleep(10)

driver.find_elements(By.TAG_NAME, 'strong')[0].get_property('innerHTML')

titleElements = driver.find_elements(By.TAG_NAME, 'strong')[0:20]

titleList = [title.get_property('innerHTML') for title in titleElements]
print(titleList)

numberElements = driver.find_elements(By.CSS_SELECTOR, '.classificacao__pontos--ponto')[0:20]

numberList = [number.get_property('innerHTML') for number in numberElements]
print(numberList)

tabela = pd.DataFrame(list(zip(titleList, numberList)), columns=['Título', 'Pontos'])

print(tabela)

tabela.to_csv('Classificação_brasileirao.csv', index=False)