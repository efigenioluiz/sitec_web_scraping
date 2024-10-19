from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

service = Service(executable_path='./chromedriver')
navegador = webdriver.Chrome(service=service)

navegador.get('https://www.rottentomatoes.com');

sleep(5)
itens = navegador.find_elements(By.XPATH, '//ul[@slot="list-items"]/li')

for item in itens:
    titulo = item.find_element(By.CLASS_NAME, 'dynamic-text-list__item-title').text
    try:
        porcentagem = item.find_element(By.XPATH, './/rt-text').text.strip()
    except:
        porcentagem = "N/A"

    print(f'Título: {titulo}, Porcentagem: {porcentagem}')

input()


