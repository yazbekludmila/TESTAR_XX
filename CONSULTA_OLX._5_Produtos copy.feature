@Consulta_Produtos_olx

Feature: Consulta e imprime consulta de 5 produtos do site da OLX
    Eu como usuario da internet consulto produtos no site da OLX 
    
    """Feature Description"""

   Background: Estar no site da OLX
     Given eu esteja na Home Page do site da OLX https://www.olx.com.br/
   
   @Consulta_5_Produtos
   Scenario: Consultar 5 primeiros produtos da OLX
      When digitar produto a ser pesquisado
      When clicar na lupa consultar
      Then visualizo produtos da pesquisa realizada
      Then vejo impressos os títulos e valores dos primeiros 5 produtos pesquisados   
  