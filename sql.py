import pyautogui as auto
import time
import keyboard
import random

keyboard.press_and_release('alt + tab')
time.sleep(1)

keyboard.press_and_release('ctrl + n')
time.sleep(1)

keyboard.press_and_release('ctrl + u')
auto.write('mpub_adm_fonte01')
time.sleep(1)
keyboard.press('enter')


auto.typewrite('Select * From LIC_CONTRATO\n  Left Join LIC_COMPRA On LIC_COMPRA.COM_COD = LIC_CONTRATO.COM_COD\n  Left Join LIC_LICITACAO On LIC_LICITACAO.LIC_COD = LIC_CONTRATO.LIC_COD\n  Left Join LIC_PREGAO On LIC_PREGAO.PRG_COD = LIC_CONTRATO.PRG_COD', 0.1)

