from constants import SCREEN_WIDTH, SCREEN_HEIGHT
import os
import time

def nice_print(str, sleep=0.05):
    for _ in str:
        print(_, end='', flush=True)
        time.sleep(sleep)


def configure_terminal_size():
    size = os.get_terminal_size()
    if size.columns != SCREEN_WIDTH or size.lines != SCREEN_HEIGHT:
        cmd = f'mode {SCREEN_WIDTH},{SCREEN_HEIGHT+3}'
        os.system(cmd)
        return
    else:
        return
