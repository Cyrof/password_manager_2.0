import os 
import time 
import platform

# os.system("python -m venv psv2")
# time.sleep(2)

# if platform.system() == "Windows":
#     os.system("psv2/Scripts/activate")
# elif platform.system() == "Linux":
#     os.system("source ./psv2/bin/activate")

# time.sleep(1)
# os.system("pip install -r requirements.txt")
os.system("cd password_manager_2.0")
os.system("docker rm psv2")
time.sleep(1)
os.system("docker rmi psv")
time.sleep(1)
os.system("docker build -t psv .")
time.sleep(1)
os.system("docker run -i -t --name psv2 psv")