from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

servico = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=servico)

# Entrar no site de viagens
driver.get('https://www.tripadvisor.com.br/')

# Achar a barra de busca e digitar o destino Nova York
driver.find_element(
    By.XPATH, '//*[@id="lithium-root"]/main/div[3]/div/div/div[2]/form/input[1]'
).send_keys('Nova York', Keys.ENTER)

# Sobre o Local
resumo = driver.find_element(
    By.XPATH, '//*[@id="lithium-root"]/main/div[6]/div/div/div[2]/div'
).get_attribute('wholeText')

# O que o local tem a oferecer
driver.find_element(
    By.XPATH,
    '//*[@id="lithium-root"]/main/div[7]/div[1]/div[2]/div[1]/div/div[1]/a/span'
).click()

# Guia turistico mais vendido
driver.find_element(
    By.CLASS_NAME, 'bsLRU btBEK fUpii'
).click()

sobre_escursao = driver.find_element(
    By.XPATH, '//*[@id="tab-data-WebPresentation_PoiAboutWeb"]/div/div/span/div[2]/div[1]/div[1]/div/div[1]/div/span/text()'
).get_attribute('wholeText')

tragetoria = driver.find_element(
    By.XPATH, '/html/body/div[5]/div/div[2]/div/div[2]/div[4]/div/span/text()'
).get_attribute('wholeText')


with open('ProBot/viagnes.txt', 'w') as arquivo:
    arquivo.writelines('Sobre Nova York \n')
    arquivo.write('\n')
    arquivo.write('\n')

    arquivo.write(resumo)
    arquivo.write('\n')
    arquivo.write('\n')

    arquivo.writelines('Escursão \n')
    arquivo.write(sobre_escursao)
    arquivo.write('\n')
    arquivo.write('\n')

    arquivo.writelines('Como sera a tragetoria \n')
    arquivo.write(tragetoria)
