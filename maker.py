import pyautogui as auto
import time
import keyboard
import random

auto.FAILSAFE = True

def moveAndClick(x, y, clicks):
    auto.moveTo(x, y, 2)
    if clicks == 1:
        auto.click()
    if clicks == 2:
        auto.doubleClick()

def write(text):
    auto.write(text, 0.1)

def abreFluxo(nomeFluxo):
    moveAndClick(1474, 145, 1) #clica na aba de fluxos
    moveAndClick(1474, 114, 1) #clica no campo de pesquisa
    keyboard.press_and_release('ctrl + A')
    write(nomeFluxo)
    moveAndClick(1474, 230, 2) #abre o fluxo

def cancelar():
    keyboard.press_and_release('alt + f4')

def clicaGrid(linha, coluna): #clica na grid (fluxo) de acordo com a linha x coluna passado por parâmetro (tipo = (1)processamento ou (2)menssagem)
    moveAndClick(1460 + 190 * (coluna-1), 137.5 + 75 * (linha-1), 2)
    time.sleep(10)
    cancelar()

'''
with open('EPRO - Controle de Documentos Atribuir Processo.txt', 'r') as file:

    for line in file:
        print(line, end='')
'''


#abreFluxo('EPRO - controle de documentos atribuir processo')
'''
try:
    while True:
        clicaGrid(2, 2)
        clicaGrid(2, 3)
        clicaGrid(3, 2)
        clicaGrid(4, 2)
        clicaGrid(4, 3)
        clicaGrid(5, 2)
        clicaGrid(5, 3)
        clicaGrid(6, 2)
        clicaGrid(6, 3)
        clicaGrid(7, 2)
        clicaGrid(7, 1)
except keyboardInterrupt:
    pass
'''

try:
    while True:
        auto.moveTo(random.randint(0,1362), random.randint(86, 722), 1)
except KeyboardInterrupt:
    pass

#auto.moveTo(1362, 722, 1)


'''
abreFluxo('EPRO - controle de documentos envia email')
while True:
    clicaGrid(2, 1)
    clicaGrid(3, 1)
    clicaGrid(4, 1)
    clicaGrid(5, 1)
    clicaGrid(6, 1)
    clicaGrid(7, 1)
'''