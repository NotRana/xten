import pyautogui as pg
import time

time.sleep(10)
for i in range(200):
    pg.write("Fucked By Rana")
    pg.press("Enter")
    print(f"{i} message has been sended")

