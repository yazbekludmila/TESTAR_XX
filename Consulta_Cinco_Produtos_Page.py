from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from PIL import ImageGrab

class Consulta_CincoProdutos():


    def __init__(self, app):
        self.app = app
       
    def consultar_cinco_produtos(self):

         campo_pesquisar = self.app.find_element_by_id("searchtext")
         campo_pesquisar.send_keys ('aaa')  
        
         botão_lupa_consulta = self.app.find_element_by_id("searchtext").click()
         sleep(5)
         self.app.execute_script('window.scrollTo( 0, 300 );')
         sleep(9)
        
        # PEGAR NOME PRODUTO 1 
         prod_1  = self.app.find_element_by_xpath('//*[@id="ad-list"]/li[1]/a/div/div[2]/div[1]/div[1]/h2')
         nome_prod_1  = self.app.find_element_by_xpath('//*[@id="ad-list"]/li[1]/a/div/div[2]/div[1]/div[1]/h2').text
        
        # PEGAR VALOR PRODUTO 1 
         valor_1  = self.app.find_element_by_xpath('//*[@id="ad-list"]/li[1]/a/div/div[2]/div[1]/div[1]/h2')
         nome_valor_1  = self.app.find_element_by_xpath('//*[@id="ad-list"]/li[1]/a/div/div[2]/div[1]/div[1]/h2').text
         sleep(8) 
        
        #### IMPRIMIR NOME E VALOR PRODUTO 1 
         print(nome_prod_1)
         print(nome_valor_1)
                
         self.app.execute_script('window.scrollTo( 0, 1000 );')

        # PEGAR NOME PRODUTO 2 
         prod_2  = self.app.find_element_by_xpath('//*[@id="ad-list"]/li[2]/a/div/div[2]/div[1]/div[1]/h2')
         nome_prod_2  = self.app.find_element_by_xpath('//*[@id="ad-list"]/li[2]/a/div/div[2]/div[1]/div[1]/h2').text
         sleep(8) 

        # PEGAR VALOR PRODUTO 2 
         valor_2  = self.app.find_element_by_xpath('//*[@id="ad-list"]/li[2]/a/div/div[2]/div[1]/div[2]/div[2]/div[1]/span')
         nome_valor_2  = self.app.find_element_by_xpath('//*[@id="ad-list"]/li[2]/a/div/div[2]/div[1]/div[2]/div[2]/div[1]/span').text
         sleep(8) 
        
        #### IMPRIMIR NOME E VALOR PRODUTO 2 
         print(nome_prod_2)
         print(nome_valor_2)
        
         self.app.execute_script('window.scrollTo( 0, 30000 );')

        # PEGAR NOME PRODUTO 3 
         prod_3  = self.app.find_element_by_xpath('//*[@id="ad-list"]/li[5]/a/div/div[2]/div[1]/div[1]/h2')
         nome_prod_3  = self.app.find_element_by_xpath('//*[@id="ad-list"]/li[5]/a/div/div[2]/div[1]/div[1]/h2').text
         sleep(8) 

        # PEGAR VALOR PRODUTO 3
         valor_3  = self.app.find_element_by_xpath('//*[@id="ad-list"]/li[5]/a/div/div[2]/div[1]/div[2]/div[2]/div[1]/span')
         nome_valor_3  = self.app.find_element_by_xpath('//*[@id="ad-list"]/li[5]/a/div/div[2]/div[1]/div[2]/div[2]/div[1]/span').text
         sleep(8) 

        #### IMPRIMIR NOME E VALOR PRODUTO 3 
         print(nome_prod_3)
         print(nome_valor_3)

        # PEGAR NOME PRODUTO 4
         prod_4  = self.app.find_element_by_xpath('//*[@id="ad-list"]/li[6]/a/div/div[2]/div[1]/div[1]/h2')
         nome_prod_4  = self.app.find_element_by_xpath('//*[@id="ad-list"]/li[6]/a/div/div[2]/div[1]/div[1]/h2').text
         sleep(8) 
        
        # PEGAR VALOR PRODUTO 4
         valor_4  = self.app.find_element_by_xpath('//*[@id="ad-list"]/li[6]/a/div/div[2]/div[1]/div[2]/div[2]/div[1]/span')
         nome_valor_4  = self.app.find_element_by_xpath('//*[@id="ad-list"]/li[6]/a/div/div[2]/div[1]/div[2]/div[2]/div[1]/span').text
         sleep(8) 

        #### IMPRIMIR NOME E VALOR PRODUTO 4 
         print(nome_prod_4)
         print(nome_valor_4)
        
         self.app.execute_script('window.scrollTo( 0, 1000 );')

        # PEGAR NOME PRODUTO 5 
         prod_5  = self.app.find_element_by_xpath('//*[@id="ad-list"]/li[7]/a/div/div[2]/div[1]/div[1]/h2')
         nome_prod_5  = self.app.find_element_by_xpath('//*[@id="ad-list"]/li[7]/a/div/div[2]/div[1]/div[1]/h2').text
         sleep(8) 

        # PEGAR VALOR PRODUTO 5
         valor_5  = self.app.find_element_by_xpath('//*[@id="ad-list"]/li[7]/a/div/div[2]/div[1]/div[2]/div[2]/div[1]/span')
         nome_valor_5  = self.app.find_element_by_xpath('//*[@id="ad-list"]/li[7]/a/div/div[2]/div[1]/div[2]/div[2]/div[1]/span').text
         sleep(8) 

        #### IMPRIMIR NOME E VALOR PRODUTO 5 
         print(nome_prod_5)
         print(nome_valor_5)
         sleep(8)     