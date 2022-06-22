# Press R for start
# Press E for break
# mr_sajt author - Edit BigEmo


import pyautogui as pg
import keyboard
while True:
    if keyboard.is_pressed('R') == True:
        while True:
            pg.click()
            if keyboard.is_pressed('E') == True:
                break
