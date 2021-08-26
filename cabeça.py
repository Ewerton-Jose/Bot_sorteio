# Importações e Defs
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
from selenium.webdriver.firefox.webdriver import WebDriver
import random

# Dados
user = 'pintocu'
senha = 'bostamijo'
foto = 'https://www.instagram.com/p/CSobtcuLYNK/'
frase = 'que fera'

# Abrir Navegador
cwd = os.getcwd()
driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
driver.get('https://www.instagram.com/')
time.sleep(2)

# Login
botão_nome = driver.find_element_by_xpath("//input[@name='username']")
botão_nome.click()
botão_nome.clear()
botão_nome.send_keys(user)
time.sleep(2)

botão_senha = driver.find_element_by_xpath("//input[@name='password']")
botão_senha.click()
botão_senha.clear()
botão_senha.send_keys(senha)
botão_senha.send_keys(Keys.RETURN)
time.sleep(5)

# assessar foto
driver.get(foto)

# Seguir, curtir, Comentar
time.sleep(2)
campo_comentario = driver.find_element_by_class_name("Ypffh")
time.sleep(random.randint(2,5))
campo_comentario.send_keys(frase)
time.sleep(random.randint(30,120))
driver.find_element_by_xpath("//button[contains(text(),'Publicar')]").click()



print('fim')
