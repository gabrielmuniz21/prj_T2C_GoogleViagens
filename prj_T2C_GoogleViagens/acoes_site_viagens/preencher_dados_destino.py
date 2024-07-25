import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from botcity.web import WebBot, Browser

class PreencherDadosDestino:
    def __init__(self, botWebbot:WebBot=None):
        self.var_botWebbot = botWebbot

    def preencher(self, arg_tplQueueItem):
        # De onde
        pesquisa = self.var_botWebbot.find_element('//input[@aria-label="De onde?"]', By.XPATH)
        pesquisa.clear()
        pesquisa.send_keys('São Paulo')
        time.sleep(2)
        
        resultado_pesquisa = self.var_botWebbot.find_element('/html/body/c-wiz[2]/div/div[2]/div/c-wiz/div[2]/div/div/div[1]/div[1]/section/div/div[1]/div[1]/div[1]/div[2]/div[1]/div/div[1]/div/div[2]/div[3]/ul/li[1]', By.XPATH)
        resultado_pesquisa.click()

        # para onde
        pesquisa = self.var_botWebbot.find_element('//input[@aria-label="Para onde?"]', By.XPATH)
        pesquisa.send_keys(arg_tplQueueItem[1])
        time.sleep(2)

        # Escolher o país com o ícone de globo
        pais_com_globo = self.var_botWebbot.find_element(f'//li[@aria-label="{arg_tplQueueItem[1]}"]', By.XPATH)
        pais_com_globo.click()

        #Click no campo de data
        input_data = self.var_botWebbot.find_element('//div[@title="Viagem de uma semana nos próximos seis meses"]', By.XPATH)
        input_data.click()
        time.sleep(2)
        
        #Click na aba Datas específicas
        aba_data_especifica = self.var_botWebbot.find_element('//*[@id="sNlbpb"]', By.XPATH)
        aba_data_especifica.click()
        time.sleep(2)
        
        #Click no input data Início
        data_inicio_input = self.var_botWebbot.find_element('//*[@id="ow78"]/div[2]/div/div[2]/div/div[2]/span/div/div[1]/div/div[1]/div/input', By.XPATH)
        data_inicio_input.send_keys('20/08/2024')
        data_inicio_input.send_keys(Keys.ENTER)
        time.sleep(2)
        
        #Click no input data Fim
        data_fim_input = self.var_botWebbot.find_element('//*[@id="ow78"]/div[2]/div/div[2]/div/div[2]/span/div/div[1]/div/div[2]/div/input', By.XPATH)
        data_fim_input.send_keys('23/08/2024')
        data_fim_input.send_keys(Keys.ENTER)
        time.sleep(2)
        
        #Click no botão Confirmar
        botao_concluido = self.var_botWebbot.find_element('(//span[text()="Concluído"])[2]', By.XPATH)
        botao_concluido.click()   
 