from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

service = Service(executable_path='./chromedriver')
navegador = webdriver.Chrome(service=service)

navegador.get('https://www.google.com');

search_box = navegador.find_element(By.NAME, 'q')

search_box.send_keys('IFPR paranaguá')

search_box.send_keys(Keys.RETURN)

first_result = navegador.find_element(By.XPATH, '(//h3)[1]')
first_result.click()

titulos =  navegador.find_elements(By.XPATH, '//h2 | //h3')

for t in titulos[:5]:
    print(t.text)

input()


