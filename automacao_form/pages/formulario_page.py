from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


class FormularioPage:
    """Page Object para o formulário de contato"""
    
    # Locators
    CAMPO_NOME = (By.NAME, "nome")
    CAMPO_EMAIL = (By.NAME, "email")
    CAMPO_TELEFONE = (By.NAME, "telefone")
    CAMPO_CIDADE = (By.NAME, "cidade")
    CAMPO_BAIRRO = (By.NAME, "bairro")
    CAMPO_MENSAGEM = (By.NAME, "mensagem")
    BOTAO_ENVIAR = (By.CSS_SELECTOR, "button[type='submit']")
    
    # Radio buttons de escolaridade
    RADIO_FUNDAMENTAL = (By.CSS_SELECTOR, "input[name='escolaridade'][value='Fundamental']")
    RADIO_MEDIO = (By.CSS_SELECTOR, "input[name='escolaridade'][value='Médio']")
    RADIO_SUPERIOR = (By.CSS_SELECTOR, "input[name='escolaridade'][value='Superior']")
    RADIO_POS = (By.CSS_SELECTOR, "input[name='escolaridade'][value='Pós-graduação']")
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def acessar_formulario(self, url):
        """Acessa a página do formulário"""
        self.driver.get(url)
        self.wait.until(EC.presence_of_element_located(self.CAMPO_NOME))
    
    def preencher_nome(self, nome):
        """Preenche o campo nome"""
        campo = self.wait.until(EC.presence_of_element_located(self.CAMPO_NOME))
        campo.clear()
        campo.send_keys(nome)
    
    def preencher_email(self, email):
        """Preenche o campo email"""
        campo = self.driver.find_element(*self.CAMPO_EMAIL)
        campo.clear()
        campo.send_keys(email)
    
    def preencher_telefone(self, telefone):
        """Preenche o campo telefone"""
        campo = self.driver.find_element(*self.CAMPO_TELEFONE)
        campo.clear()
        campo.send_keys(telefone)
    
    def preencher_cidade(self, cidade):
        """Seleciona a cidade no dropdown"""
        select_element = self.driver.find_element(*self.CAMPO_CIDADE)
        select = Select(select_element)
        select.select_by_visible_text(cidade)
    
    def preencher_bairro(self, bairro):
        """Preenche o campo bairro"""
        campo = self.driver.find_element(*self.CAMPO_BAIRRO)
        campo.clear()
        campo.send_keys(bairro)
    
    def selecionar_escolaridade(self, escolaridade):
        """Seleciona o radio button de escolaridade"""
        mapeamento = {
            'Fundamental': self.RADIO_FUNDAMENTAL,
            'Médio': self.RADIO_MEDIO,
            'Superior': self.RADIO_SUPERIOR,
            'Pós-graduação': self.RADIO_POS
        }
        
        locator = mapeamento.get(escolaridade, self.RADIO_MEDIO)
        radio = self.driver.find_element(*locator)
        radio.click()
    
    def preencher_mensagem(self, mensagem):
        """Preenche o campo mensagem"""
        campo = self.driver.find_element(*self.CAMPO_MENSAGEM)
        campo.clear()
        campo.send_keys(mensagem)
    
    def clicar_enviar(self):
        """Clica no botão enviar"""
        botao = self.driver.find_element(*self.BOTAO_ENVIAR)
        botao.click()
    
    def verificar_escolaridade_selecionada(self, escolaridade):
        """Verifica se a escolaridade está selecionada"""
        mapeamento = {
            'Fundamental': self.RADIO_FUNDAMENTAL,
            'Médio': self.RADIO_MEDIO,
            'Superior': self.RADIO_SUPERIOR,
            'Pós-graduação': self.RADIO_POS
        }
        
        locator = mapeamento.get(escolaridade, self.RADIO_MEDIO)
        radio = self.driver.find_element(*locator)
        return radio.is_selected()