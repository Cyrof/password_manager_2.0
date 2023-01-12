# python file which handles encryption and decryption

from cryptography.fernet import Fernet
from dotenv import load_dotenv, set_key, get_key, unset_key
import os
import hashlib

class Crypto:
    # class crypto to handle encryption and decryption
    
    def __init__(self):
        """ instance initialization for crypto class 
        """
        self.check_env()
        self.__envpath = os.path.abspath('psv2.env')
        load_dotenv(self.__envpath)     

    def check_env(self):
        """create env file if not exists
        :param:
        :return:
        """
        with open('psv2.env', 'a') as f:
            f.close()

    def check_key(self):
        """ function to check if key exists
        :param:
        :return: true if key exists else false
        """

        if os.getenv('KEY'):
            return True
        else:
            return False
        
    def generate_key(self):
        """ function to generate key
        :param:
        :return: 
        """
        if not self.check_key():
            key = Fernet.generate_key()
            key_str = str(key, "utf-8")
            os.environ['KEY'] = key_str
            set_key(self.__envpath, 'KEY', key_str)  

    def check_master(self):
        """ function to check if master key exists
        :param:
        :return: true if master key exists else false
        """

        if os.getenv('MASTER'):
            return True
        else:
            return False

    def generate_master(self, master_password):
        """ function to generate master key
        :param master_password: master password for the program
        :return: 
        """
        if not self.check_master():
            sha256_mp = hashlib.sha256(master_password.encode()).hexdigest() 
            os.environ['MASTER'] = sha256_mp
            set_key(self.__envpath, 'MASTER', sha256_mp)
        else:
            print("Master key already exists")

if __name__ == "__main__":
    c = Crypto()
    c.generate_master('hello')
    