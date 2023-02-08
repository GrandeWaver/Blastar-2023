import os
import sys
import time

from modules import nice_print

# THANKS <3 https://stackoverflow.com/questions/3173320/text-progress-bar-in-terminal-with-block-characters
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()


nice_print("STARTING....", .05)


for i in range(0, 5):
    # Do nothing...
    time.sleep(0.1)
    # Update Progress Bar
    printProgressBar(i + 1, 5, prefix = 'Progress:', suffix = 'Complete', length = 50)


nice_print("processing....", .05)
syms = ['\\', '|', '/', '-']
bs = '\b'


for _ in range(3):
    for sym in syms:
        sys.stdout.write("\b%s" % sym)
        sys.stdout.flush()
        time.sleep(.2)


print("", end= "\r")


for i in range(0, 3):
    # Do nothing...
    time.sleep(0.1)
    # Update Progress Bar
    printProgressBar(i + 1, 3, prefix = 'Progress:', suffix = 'Complete', length = 50)

# clear console
os.system('cls')