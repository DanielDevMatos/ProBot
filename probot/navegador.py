from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def drive():
    servico = Service(ChromeDriverManager().install())
    navegador = webdriver.Chrome(service=servico)
