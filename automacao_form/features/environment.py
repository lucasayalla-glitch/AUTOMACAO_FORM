from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def before_all(context):
    """Executa antes de todos os testes"""
    context.url = "https://formulario-contato-m8p8.onrender.com/"


def before_scenario(context, scenario):
    """Executa antes de cada cenário"""
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')  # Descomente para modo headless
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--start-maximized')
    
    service = Service(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(service=service, options=options)


def after_scenario(context, scenario):
    """Executa após cada cenário"""
    time.sleep(2)  # Aguarda para visualizar
    context.driver.quit()