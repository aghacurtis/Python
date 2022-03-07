import pyautogui as pt
import keyboard
from time import sleep

def nav_to_image(image, clicks, off_x=0, off_y=0):
    position = pt.locateCenterOnScreen(image, confidence=.7)
    
    if position is None:
        print(f'{image} not found....')
        return 0
    else:
        pt.moveTo(position, duration =.1)
        pt.moveRel(off_x, off_y, duration =.1)
        pt.click(clicks=clicks, interval=.3)
        

sleep(1)
while True:
    nav_to_image('image/cookie.png', 3)
    pt.click()
    if keyboard.is_pressed('w'):
       quit()

