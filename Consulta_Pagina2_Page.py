from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from PIL import ImageGrab

class Consulta_Pagina2():
   
    def __init__(self, app):
        self.app = app
   
    def consultar_pagina2(self):
        campo_pesquisar = self.app.find_element_by_id("searchtext")
        campo_pesquisar.send_keys ('aaa')  

        botão_lupa_consulta = self.app.find_element_by_id("searchtext").click()
        sleep(5)
        self.app.execute_script('window.scrollTo( 0, 9990000 );')
        sleep(9)
         
        BOTÃO PAGINA 2  
        botao_pagina2  = self.app.find_element_by_xpath('//*[@id="column-main-content"]/div[19]/div/div[1]/ul/li[2]').click()
        sleep(8) 

 #### PAGINA 2 == PRIMEIRO PRODUTO 
      
        self.app.execute_script('window.scrollTo( 0, 1000 );')
        prod1_pagina1 = self.app.find_element_by_xpath('//*[@id="listing-gallery-ads"]/div/div[2]/div/div/div[2]/div/div[1]/div/div/a/div[1]/img').click()
       
        sleep(15)
        self.app.execute_script('window.scrollTo( 0, 1000 );')
        ImageGrab.grab().save('PRODUTO01 PAGINA 2 OLX.png')
        sleep(5)

#       msg_valida_alteracao = self.app.find_element_by_xpath('//*[@id="managerContent"]/table/tbody/tr/td[2]/table[2]/tbody/tr[3]/td/div[1]')
#       assert msg_valida_alteracao.text == 'Registro alterado com sucesso.' 
