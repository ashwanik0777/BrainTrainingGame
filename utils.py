import os
import platform
import time

def clear_screen():
    cmd = 'cls' if platform.system().lower().startswith('win') else 'clear'
    os.system(cmd)

def safe_input(prompt=''):
    return input(prompt)

def short_pause(seconds=0.5):
    time.sleep(seconds)