from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time 
import datetime
import random

class InstagramBot: 
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(executable_path=r"C:\Users\vrteodoro\Desktop\Trabalhos\geckodriver-v0.26.0-win64\geckodriver.exe")

    def login(self):
        driver = self.driver
        driver.get('https://www.instagram.com/')
        time.sleep(3)

        campo_usuario = driver.find_element_by_xpath("//input[@name='username']")
        campo_usuario.click()
        campo_usuario.clear()
        campo_usuario.send_keys(self.username)

        campo_senha = driver.find_element_by_xpath("//input[@name='password']")
        campo_senha.click()
        campo_senha.clear()
        campo_senha.send_keys(self.password)
        campo_senha.send_keys(Keys.RETURN)

        time.sleep(5)
        #Código da foto (URL)
        self.comentar_foto('CBopyICh2A_')

    @staticmethod
    def digite_como_uma_pessoa(frase, onde_digitar):
        for letra in frase:
            onde_digitar.send_keys(letra)
            time.sleep(random.randint(1,5)/30)

    def comentar_foto(self, hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/p/" + hashtag + "/")

        try:
            comments = ["Participando do sorteio!"]
            count = 0

            while True:
                driver.find_element_by_class_name('Ypffh').click()
                campo_comentario = driver.find_element_by_class_name('Ypffh')
                time.sleep(1)

                self.digite_como_uma_pessoa(comments[count], campo_comentario)
                time.sleep(random.randint(50,150))
                driver.find_element_by_xpath("//button[contains(text(), 'Publicar')]").click()
                time.sleep(5)     
                count = count + 1
                print('COUNT:', count, ' TIME:', datetime.datetime.now().strftime("%H:%M:%S"))
                
        except Exception as e:
            print(e)

#Insira seus dados aqui
victorBot = InstagramBot('login', 'senha')
victorBot.login()