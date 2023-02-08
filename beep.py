import os
import winsound
import time

def start_procedure():
    for i in range(3,0, -1):
        os.system('cls')
        print(i)
        winsound.Beep(1000, 500)
        time.sleep(0.5)        
    winsound.Beep(1000, 1000)
    os.system('cls')      


def sos():                
    winsound.Beep(2000, 300)   
    winsound.Beep(1500, 300)    
    winsound.Beep(1000, 600) 




