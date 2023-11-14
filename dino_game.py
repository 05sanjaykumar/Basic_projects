import pyautogui as pt #make sure you install all these modules
import time
import keyboard
time.sleep(2) ''' to make sure that we have sufficient time to change the screen and go to  webpage from our editorial to load the dino game, you can change time to still 
more seconds if the transition is slower '''
while True:
    im = pt.screenshot()
    screen = im.getpixel((300,200))#place the values at the background of the screen

    x1 = im.getpixel((516,237))#place according where you find plants
    x2 = im.getpixel((500,243))
    x3 = im.getpixel((525,220))
    x4 = im.getpixel((530,238))

    if screen[0] == 32 or screen[0]==255: #The background values may be black or white, during the time of that background color we are performing the if conditions
        if x1[0]==172 or x2[0]==172 or x3[0]==172 or x4[0]==172: #after having the background values, if we have this values, this represents the color of the objects, if we
            pt.press('space') # -find these values we need to press space, at the color 172 we are jumping
            time.sleep(0.5)
    else:
        pass

    if keyboard.is_pressed('s'): # to terminate the code when we press s on our keyboard, if we change to any values as we like
        break
    else:
        pass
