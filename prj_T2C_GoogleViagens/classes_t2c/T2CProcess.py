from botcity.web import WebBot, Browser
from botcity.core import DesktopBot
from prj_T2C_GoogleViagens.acoes_site_viagens.preencher_excel_viagens import PreencherExcelViagens
from prj_T2C_GoogleViagens.classes_t2c.utils.T2CMaestro import T2CMaestro
from prj_T2C_GoogleViagens.acoes_site_viagens.extrair_informacoes import ExtrairInformacoes
from prj_T2C_GoogleViagens.acoes_site_viagens.preencher_dados_destino import PreencherDadosDestino 

class T2CProcess:
    def __init__(self, arg_dictConfig:dict, arg_clssMaestro:T2CMaestro, arg_botWebbot:WebBot=None, arg_botDesktopbot:DesktopBot=None):
        if(arg_botWebbot is None and arg_botDesktopbot is None): 
            raise Exception("Não foi possível inicializar a classe, forneça pelo menos um bot")
        else:
            self.var_botWebbot = arg_botWebbot
            self.var_botDesktopbot = arg_botDesktopbot
            self.var_dictConfig = arg_dictConfig
            self.var_clssMaestro = arg_clssMaestro
            
            self.preencher_dados_destino = PreencherDadosDestino(self.var_botWebbot)
            self.extrair_informacoes = ExtrairInformacoes(self.var_botWebbot)
            self.preencher_excel_viagens = PreencherExcelViagens()
   
    def execute(self, arg_tplQueueItem:tuple):
        # Preencher dados
        self.preencher_dados_destino.preencher(arg_tplQueueItem)
             
        # Chamada para classe de extrair dados da cidade
        var_listCidades = self.extrair_informacoes.extrair(arg_tplQueueItem[1])
        
        # Salvar os dados em um arquivo Excel
        self.preencher_excel_viagens.salvarTodos(var_listCidades)
