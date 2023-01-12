import os 
import time 
import platform

os.system("python -m venv psv2")
time.sleep(2)

if platform.system() == "Windows":
    os.system("psv2/Scripts/activate")
elif platform.system() == "Linux":
    os.system("source ./psv2/bin/activate")

