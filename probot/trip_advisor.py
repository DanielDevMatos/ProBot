from probot.navegador import drive
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Entrar no site de viagens
driver = drive()
driver.get('https://www.tripadvisor.com.br/')

# Achar a barra de busca e digitar o destino Nova York
driver.find_element(
    By.XPATH, '//*[@id="lithium-root"]/main/div[3]/div/div/div[2]/form/input[1]'
).send_keys('Nova York', Keys.ENTER)

# Sobre o Local
resumo = driver.find_element(
    By.XPATH, '//*[@id="lithium-root"]/main/div[6]/div/div/div[2]/div'
).get_attribute('textContent')

# O que o local tem a oferecer
driver.find_element(
    By.XPATH,
    '//*[@id="lithium-root"]/main/div[7]/div[1]/div[2]/div[1]/div/div[1]/a/span'
).click()

# Guia turistico mais vendido
driver.find_element(
    By.XPATH, '//*[@id="lithium-root"]/main/span/div/div[3]/div/div[2]/div[2]/span/div/div[1]/section[3]/div/div/span/div/div/div[2]/div/div[2]/div/ul/li[1]/span/span/div/a/div[2]/div[2]/div'
).click()

sobre_escursao = driver.find_element(
    By.XPATH, '//*[@id="tab-data-WebPresentation_PoiAboutWeb"]/div/div/span/div[2]/div[1]/div[1]/div/div[1]/div/span'
).get_attribute('textContent')

tragetoria = driver.find_element(
    By.XPATH, '/html/body/div[5]/div/div[2]/div/div[2]/div[4]/div/span'
).get_attribute('textContent')

with open('ProBot/viagnes.txt', 'w') as arquivo:
    arquivo.writelines('Sobre Nova York')
    arquivo.write('')
    arquivo.write('')
    arquivo.write(resumo)
    arquivo.write('')
    arquivo.write('')
    arquivo.write(sobre_escursao)
    arquivo.write('')
    arquivo.write('')
    arquivo.write(tragetoria)
