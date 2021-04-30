@Consulta_Primeiro_Produto_pagina2_OLX

Feature: Consulta e imprime primeiro produto da página 2
    Eu como usuario da internet consulto primeiro produto da página 2
    
    """Feature Description"""

   Background: Estar no site da OLX
     Given eu esteja na Home Page do site da OLX https://www.olx.com.br/
  
   @Consulta_Produto1_Pagina2_OLX
   Scenario: Consultar primeiro produto da pagina 2
      When digitar produto a ser pesquisado pagina 2
      When clicar na lupa consultar
      Then visualizo produtos da pesquisa realizada
      
      When clico no numero da pagina 2  
      Then visualizo primeiro produto da página 2 e imprimo anuncio