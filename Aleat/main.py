import pyautogui as auto
import time
import random

timer = 30

def move_and_click(x_axis, y_axis, clicks):
    auto.moveTo(x_axis, y_axis, 2)
    if clicks == 1:
        auto.click()
    if clicks == 2:
        auto.doubleClick()
    time.sleep(5)


def alt_tab():
    auto.keyDown('alt')
    time.sleep(.2)

    for i in range(random.randint(1, 5)):
        auto.press('tab')

    time.sleep(.3)
    auto.keyUp('alt')


print(f"Aguardando timer de {timer}s antes de começar...")
time.sleep(timer)
print("Programa iniciado")

width, height = auto.size()

print(f"Resolução: ({width}, {height})")


try:
    while True:
        x = random.randint(1, 100)
        if x <= 80:
            move_and_click(random.randint(0, width), random.randint(86, height), 1)
        if x > 80:
            alt_tab()
except KeyboardInterrupt:
    pass
