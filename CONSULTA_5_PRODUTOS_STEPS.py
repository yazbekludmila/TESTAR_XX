from pages.pages.Abrir_Site_Page  import Abrir_Site
from pages.pages.Efetuar_Login_Page import Fazer_Login
from pages.pages.Consulta_Cinco_Produtos_Page import Consulta_CincoProdutos
###################################################################

@when(u'digitar produto a ser pesquisado')
def step_impl(context):
   context.consultacincoprodutos.consultar_cinco_produtos()

@when(u'clicar na lupa consultar')
def step_impl(context):
   pass

@then(u'visualizo produtos da pesquisa realizada')
def step_impl(context):
   pass

@then(u'vejo impressos os títulos e valores dos primeiros 5 produtos pesquisados')
def step_impl(context):
   pass
