from scripts.menu import Menu
from scripts.logger import Log
import os
from termcolor import colored
import time
import sys
from inputimeout import inputimeout


logger = Log()



def run():
    try:
        app = Menu()
        logger.add_info("Application running... @8-main.py")
        app.run()
    except Exception as e:
        logger.add_error(e)
        print("An error occurred" + e)

def check():
    
    try:
        start = inputimeout(prompt="Start? [y/n]: ", timeout=30)
        print(colored("Program starting...", 'cyan'))

        if start == 'n':
            print(colored("Program ending...", 'red'))
            sys.exit()
        else:
            print(colored("Program starting...", 'cyan'))
            
    except Exception:
        print(colored("Program ending...", 'red'))
        sys.exit()
            

if __name__ == '__main__':
    check()
    run()