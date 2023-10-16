import pyautogui 
import time

while 1:
    if pyautogui.locateOnScreen('end.png', confidence=0.9) != None:
        print("I can see it")
        time.sleep(0.5)
    else:
        print("I am unable to see it")
        time.sleep(0.5)