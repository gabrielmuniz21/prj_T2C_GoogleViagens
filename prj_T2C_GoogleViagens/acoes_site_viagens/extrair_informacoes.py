import time
from selenium.webdriver.common.by import By
from botcity.web import WebBot, Browser

class ExtrairInformacoes:
    def __init__(self, botWebbot:WebBot=None):
        self.botWebbot = botWebbot

    def extrair(self, pais):
        index = 1
        info_cidades = []
        
        #Armazenar cidades que já passaram no while        
        cidades_vistas = set()
        
        while True:               
            xpath_nome_cidade = f'/html/body/c-wiz[2]/div/div[2]/div/c-wiz/div[2]/div/div/div[1]/main/div/div[2]/div/ol/li[{index}]/div/div[2]/div[1]/h3'
            xpath_preco_cidade = f'//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/div/c-wiz/div[2]/div/div/div[1]/main/div/div[2]/div/ol/li[{index}]/div/div[2]/div[2]/div[1]/div[1]/span'
            
            try:                
                nome_cidade = self.botWebbot.find_element(xpath_nome_cidade, By.XPATH).text
                preco_cidade = self.botWebbot.find_element(xpath_preco_cidade, By.XPATH).text
            
                # Adicionar o nome da cidade à lista
                cidades_vistas.add(nome_cidade)

                # Adicionar os dados à lista
                cidade_preço = {
                    'País': pais,
                    'Cidade': nome_cidade,
                    'Preço': preco_cidade
                }
                
                info_cidades.append(cidade_preço)
                print("Dados coletados:", cidade_preço)
                index += 1
                time.sleep(2)
            except Exception as e:
                print("Elemento não encontrado. Encerrando o loop.")
                break
        
        return info_cidades
