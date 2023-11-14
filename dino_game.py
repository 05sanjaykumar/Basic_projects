import pyautogui as pt
import time
import keyboard
time.sleep(2)
while True:
    im = pt.screenshot()
    screen = im.getpixel((300,200))#place the values at the background of the screen

    x1 = im.getpixel((516,237))#place according where you find plants
    x2 = im.getpixel((500,243))
    x3 = im.getpixel((525,220))
    x4 = im.getpixel((530,238))

    if screen[0] == 32 or screen[0]==255:
        if x1[0]==172 or x2[0]==172 or x3[0]==172 or x4[0]==172:
            pt.press('space')
            time.sleep(0.5)
    else:
        pass

    if keyboard.is_pressed('s'):
        break
    else:
        pass
