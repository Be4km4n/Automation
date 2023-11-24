import pyautogui as auto
import time
import keyboard
import random

def moveAndClick(x, y, clicks):
    auto.moveTo(x, y, 2)
    if clicks == 1:
        auto.click()
    if clicks == 2:
        auto.doubleClick()
    time.sleep(30)

#fica clicando sem mobver o mouse
def clickWithoutMoving():
    auto.click()
    time.sleep(20)

#clica na área se uso dos aplicativos (body)
def clickAppsRandom():
    moveAndClick(random.randint(415, 764), 745, 1) #primeiros apps abertos (8 apps)

#Clica na barra de navegação
def clickTop():
    moveAndClick(random.randint(20, 1186), 12, 1)

time.sleep(40)
clickAppsRandom()

try:
    while True:
        x = random.randint(1, 10)
        if(x < 4):
            clickAppsRandom()           

        if(x == 10):
            clickTop()

        moveAndClick(random.randint(0,1362), random.randint(86, 722), 1)
except KeyboardInterrupt:
    pass
