from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

servico = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=servico)

lista = ['restaurants', 'dentists', 'Auto Repair', 'barbershops', 'lawyer', 'Hospital', 'veterinary']

# Entrar nos serviços
driver.get('https://www.yellowpages.com/')

# Procura de serviços em New York
for nome in lista:
    driver.find_element(By.XPATH, '//*[@id="query"]').send_keys(nome)
    driver.find_element(By.XPATH,
                        '//*[@id="location"]').send_keys('New York, NY', Keys.ENTER)

    # tipos de Procura
    titulo = driver.find_element(By.TAG_NAME, 'h1').get_attribute('textContent')

    h2 = driver.find_element(By.TAG_NAME, 'h2')
    for c in range(1, 3):
        # Informações do local
        nomeloja = driver.find_element(
            By.TAG_NAME, 'SPAN').get_attribute('textContent')

        endereco = driver.find_element(
            By.CLASS_NAME, 'street-address'
        ).get_attribute('innerHTML')

        localidade = driver.find_element(
            By.CLASS_NAME, 'locality'
        ).get_attribute('innerHTML')

        telefone = driver.find_element(
            By.CLASS_NAME, 'phones phone primary'
        ).get_attribute('data')

        servicos = driver.find_element(
            By.CLASS_NAME, 'categories'
        ).get_attribute('textContent')

        # Criação da pasta TXT
        with open('ProBot/servicos.txt', 'w') as arquivo:
            arquivo.writelines(titulo)
            arquivo.writelines('\n')
            arquivo.writelines('\n')

            arquivo.writelines(nomeloja)
            arquivo.writelines('\n')

            arquivo.writelines('[Endereço do local]: \n')
            arquivo.writelines(endereco)
            arquivo.writelines(localidade)
            arquivo.writelines('\n')
            arquivo.writelines('\n')

            arquivo.writelines('[Telefone]: \n')
            arquivo.writelines(telefone)
            arquivo.writelines('\n')
            arquivo.writelines('\n')

            arquivo.writelines('[serviços disponiveis]: \n')
            arquivo.writelines(servicos)
            arquivo.writelines('\n')

