from pages.pages.Abrir_Site_Page  import Abrir_Site
from pages.pages.Efetuar_Login_Page import Fazer_Login
from pages.pages.Consulta_Conteudo_Page import Consulta_Conteudo
from pages.pages.Consulta_Pagina2_Page  import Consulta_Pagina2
###################################################################
  
@when(u'digitar produto a ser pesquisado pagina 2')
def step_impl(context):
   context.consultapagina2.consultar_pagina2()
  
@when(u'clico no numero da pagina 2')
def step_impl(context):
   pass

@then(u'visualizo primeiro produto da página 2 e imprimo anuncio')
def step_impl(context):
   pass
