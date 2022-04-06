# Versão 2.0

# Defs e importações
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
from selenium.webdriver.firefox.webdriver import WebDriver
import random
from selenium.webdriver.common.by import By

# Dados
user = ''
senha = ''
foto = 'https://www.instagram.com/p/CbD5Nz2OMH7/'
amigos = ['xwaassdd1','aaddoollff','dddddd']

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
time.sleep(4)

botão_senha = driver.find_element_by_xpath("//input[@name='password']")
botão_senha.click()
botão_senha.clear()
botão_senha.send_keys(senha)
botão_senha.send_keys(Keys.RETURN)
time.sleep(6)

# assessar foto
driver.get(foto)
time.sleep(3)

# Comentar
def digite(frase, ondedigitar):
    for letra in frase:
        ondedigitar.send_keys(letra)
        time.sleep(random.randint(1,5)/30)
time.sleep(2)


fc = 0
while True:
    try:
        driver.find_element_by_class_name("Ypffh").click()
        campo_comentario = driver.find_element_by_class_name("Ypffh")
        time.sleep(random.randint(2,5))
        x = random.choice(amigos)
        digite(x,campo_comentario)
        time.sleep(random.randint(30,120))
        driver.find_element_by_class_name('_7UhW9.xLCgt.qyrsm.gtFbE.uL8Hv.T0kll').click()
        time.sleep(5)
        fc = fc + 1
    except:
        print('Error! Não publiquei')
    else:
        print(f'Comentário {fc} feito')
