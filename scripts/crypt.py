# python file which handles encryption and decryption

from cryptography.fernet import Fernet
from dotenv import load_dotenv
import os

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
        


if __name__ == "__main__":
    c = Crypto()
