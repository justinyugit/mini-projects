import numpy as np
import cv2
from mss import mss
from PIL import Image
import os
import time


#Delay of 5 seconds so game window can be opened
time.sleep(5)

sct = mss()
countFish=1
delayCount = 0

while 1:
    os.system('xdotool click 3')
    
    #Delay of 3 seconds to allow the fishing bob to settle
    time.sleep(3)
    
    while 1:
        w, h = 800, 600

        #Lower and Upper RGB bounds of the red fishing bob
        lower=np.array([36,36,189], dtype="uint8")
        upper=np.array([48,48,229], dtype="uint8")
    
        #Takes a ROI screen capture of the upper middle left half of the screen.
        monitor = {'top': 100, 'left': 100, 'width': w, 'height': h}
        img = Image.frombytes('RGB', (w,h), sct.grab(monitor).rgb)
        IMG=cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        mask=cv2.inRange(IMG, lower, upper)

        #Below can be commented out to improve performance.
        cv2.imshow('test', mask)

        #Gives user time to pull up mask window
        if(delayCount==0):
            time.sleep(10)
        delayCount+=1

        if np.sum(mask) == 0:    
            print(countFish)
            countFish+=1
            cv2.imwrite('BobBelowSurface.png', IMG)
            os.system('xdotool click 3')
            time.sleep(1)
            break
        
        
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

