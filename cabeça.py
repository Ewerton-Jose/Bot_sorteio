# Importações e Defs
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
from selenium.webdriver.firefox.webdriver import WebDriver
import random

# Dados
user = ''
senha = ''
foto = 'https://www.instagram.com/p/CT69hbnAN-q/'
amigos = ['@cdnpablo @steelcurl @j.o.n.a.t.h.a.m', '@deposito_de_creme @steelcurl @cdnpablo', '@j.o.n.a.t.h.a.m @deposito_de_creme @cdnpablo', '@steelcurl @j.o.n.a.t.h.a.m @cdnpablo']
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
time.sleep(6)

# assessar foto
driver.get(foto)
time.sleep(3)

# Seguir

"""
try:
    driver.find_element_by_xpath("//button[contains(text(),'Seguir')]").click()
    time.sleep(2)
except:
    print('Error!')
else:
    print('segui não')

"""

# curtir Publicação
"""
try:
    driver.find_element_by_xpath("//svg[@class='_8-yf5 ']").click()
    time.sleep(0.5)

except:
    print('Error2! (Não curti a publicação)')
else:
    print('tudo ok')

"""

# Comentar
def digite(frase, ondedigitar):
    for letra in frase:
        ondedigitar.send_keys(letra)
        time.sleep(random.randint(1,5)/30)
time.sleep(2)

print(len(amigos))
"""while True:
    try:
        driver.find_element_by_class_name("Ypffh").click()
        campo_comentario = driver.find_element_by_class_name("Ypffh")
        time.sleep(random.randint(2,5))
        x = random.choice(amigos)
        digite(x,campo_comentario)
        time.sleep(random.randint(30,120))
        driver.find_element_by_xpath("//button[contains(text(),'Publicar')]").click()
        time.sleep(5)
    except:
        print('Error! Não publiquei')
    else:
        print('pinto')
        """
try:
        driver.find_element_by_class_name("Ypffh").click()
        campo_comentario = driver.find_element_by_class_name("Ypffh")
        digite('pp',campo_comentario)
        time.sleep(5)
        driver.find_element_by_xpath("//button[contains(text(),'Publicar')]").click()
        driver.find_element_by_class_name("_7UhW9   xLCgt        qyrsm      gtFbE     uL8Hv        T0kll ")
except:
        print('elemento não achado')
else:
        print('element achado')
"""
<div class="">Publicar</div>
"""