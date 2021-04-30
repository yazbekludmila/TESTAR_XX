
"""		Pyautomator Framework de teste 

			TESTES OLX"""

from selenium import webdriver
from Pyautomators import fixture
from webautomators import WebChromeDriver
from webautomators.extended_options import WebChromeOptions

from pages.pages.Abrir_Site_Page  import Abrir_Site
from pages.pages.Consulta_Pagina2_Page import Consulta_Pagina2
from pages.pages.Consulta_Cinco_Produtos_Page import Consulta_CincoProdutos

def before_all(context):
	options = WebChromeOptions()
	options.maximized()
	context.app = webdriver.Chrome(executable_path='./driver/chromedriver.exe', options=options)
		 
	context.abresite                 = Abrir_Site(context.app)
	context.login                    = Fazer_Login(context.app)
	Context.consultapagina2          = Consulta_Pagina2(context.app)
	context.consultacincoprodutos    = Consulta_CincoProdutos(context.app)
	
	context.pages = {
	    "login": "https://www.olx.com.br/"
	}

def before_feature(context,feature):
	pass

def before_scenario(context,scenario):
	pass

def before_step(context,step):
	pass

def after_step(context,step):
	pass

def after_scenario(context,scenario):
	pass

def after_feature(context,feature):
	pass

#def after_all(context):
#	context.driver.quit()

