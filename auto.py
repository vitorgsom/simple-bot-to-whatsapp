from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from PIL import Image
import time, qrcode

service = Service(ChromeDriverManager( ).install())
browser = webdriver.Chrome(service=service)
browser.get('https://web.whatsapp.com/')

time.sleep(5)

div = browser.find_element('xpath', '//*[@id="app"]/div/div/div[2]/div[1]/div/div[2]/div')
name = 'qrcode.png'

def Save(name, code):
    imagem = qrcode.make(code)
    imagem.save(name)

def Open(name):
    imagem = Image.open(name)
    imagem.show()

def newCode():
    code_value = div.get_attribute("data-ref")
    return code_value

code_value = newCode()
Save(name, code_value)
Open(name)

while True:
    if code_value != div.get_attribute("data-ref"):
        code_value = newCode()
        Save(name, code_value)
        Open(name)
    else:
        print('Esperando logar')
        time.sleep(1)
