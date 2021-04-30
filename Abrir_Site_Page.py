from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


class Abrir_Site():

    def __init__(self, app):
        self.app = app
        
    def abrir_home(self):
        self.app.get('https://www.olx.com.br/')
      
    
    