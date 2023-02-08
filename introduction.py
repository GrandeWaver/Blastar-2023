import msvcrt
import time
from modules import nice_print


def introduction():
    five_seconds = time.time() + 30
    while time.time() < five_seconds:
        try: 
            nice_print("Do you need instructions (Y/N)", 0.01)
            user_input = str(input("\n"))
            if user_input == "y" or user_input == "Y":
                nice_print("\nUSE ARROWS FOR CONTROL AND SPACE TO SHOOT\n")
                time.sleep(.5)
                nice_print("\nMISSION: AVOID ALL COMETS AND GET HOME SAFELY\n\n")
                time.sleep(.5)
                nice_print("\nUSE q TO QUIT\n")
                time.sleep(.5)
            elif user_input == "n" or user_input == "N":
                pass
            else:
                raise(ValueError)
            while True:
                print("PRESS ENTER", end='\r')
                time.sleep(0.5)
                print("              ", end='\r')
                time.sleep(0.5)
                if msvcrt.kbhit():
                    if msvcrt.getwche() == '\r':
                        five_seconds = time.time()
                        break
        except ValueError:
            print(('This is not Y or N'))