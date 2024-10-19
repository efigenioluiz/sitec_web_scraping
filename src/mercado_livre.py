from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

service = Service(executable_path='./chromedriver')
navegador = webdriver.Chrome(service=service)

navegador.get('https://www.mercadolivre.com.br');
sleep(2)

search_box = navegador.find_element(By.ID, 'cb1-edit')
search_box.send_keys('notebook')
search_box.send_keys(Keys.RETURN)
sleep(2)

input()


