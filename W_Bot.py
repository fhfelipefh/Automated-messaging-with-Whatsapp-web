from selenium import webdriver
from datetime import date
from datetime import datetime
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
data_atual = date.today()

# Dependencies necessarias:
# pip install selenium
# pip install webdriver_manager

contatos = []
mensagem = []

# Caso deseja enviar uma mensagem infinitamente para os contatos digite 0, quanto menor o número de contatos mais rápido será enviado.
# Se desejar enviar a mensagem uma vez para cada contato digite 1 

loop = int(input('Mandar mensagens em loop | 0 = ininito | 1 = uma execução: '))
if loop == 0:
    print('LOOP SELECIONADO...')
else:
     print('ENVIARÁ UMA VEZ...')

arquivo = open("msg.txt","r")       # abre o arquivo txt para leitura 
for linha in arquivo:               # loop para ler tudo que tem no arquivo
    linha = linha.rstrip()          # pega uma linha do arquivo
    print(linha)                    # escreve na teLa
    mensagem.append(linha)          # adiciona a linha nas mensagens

arquivo = open("contatos.txt","r")  # abre o arquivo txt para leitura 
for linha in arquivo:               # loop para ler tudo que tem no arquivo
    linha = linha.rstrip()          # pega uma linha do arquivo
    print(linha)                    # escreve na teLa
    contatos.append(linha)          # adiciona a linha na Lista de contatos

now = datetime.now()
print("Horário de Inicio: (H/M/S)",now.hour,":",now.minute,":",now.second)
print('Iniciando envio...')
###############################################################################################
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')

#não diminua esse tempo ou a página não irá carregar
print('T-20s')
time.sleep(10)
print('T-10s')
time.sleep(5)
print('T-5s')
time.sleep(4)
print('T-4s')
time.sleep(3)
print('T-3s')
time.sleep(2)
print('T-2s')
time.sleep(1)
print('T-1s')
print('Starting...')

# buscar contatos/grupos
def buscar_contato(contato):
        campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
        #comente a linha time.sleep se quiser muito rápido
        time.sleep(1)
        campo_pesquisa.click()
        campo_pesquisa.send_keys(contato)
        campo_pesquisa.send_keys(Keys.ENTER)

def enviar_mensagem(mensagem):
        campo_mensagem = driver.find_elements_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
        campo_mensagem[1].click()
        ##Diminua o tempo entre parenteses ou aumente se precisar
        #comente a linha time.sleep se quiser muito rápido
        #time.sleep(3)
        campo_mensagem[1].send_keys(mensagem)
        campo_mensagem[1].send_keys(Keys.ENTER)

if loop == 0:
    while True:
        for contato in contatos:
            buscar_contato(contato)
            enviar_mensagem(mensagem)

if loop == 1:
    for contato in contatos:
            buscar_contato(contato)
            enviar_mensagem(mensagem)

now = datetime.now()
print("Horário de término:",now.hour,":",now.minute,":",now.second)
print("ʕ•́ᴥ•̀ʔっ")
## Developed by felipe