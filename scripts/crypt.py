# python file which handles encryption and decryption

from cryptography.fernet import Fernet
from dotenv import load_dotenv, set_key, get_key, unset_key
import os
import hashlib
from logger import Log

class Crypto:
    # class crypto to handle encryption and decryption
    
    def __init__(self):
        """ instance initialization for crypto class 
        """
        self.check_env()
        self.__envpath = os.path.abspath('psv2.env')
        load_dotenv(self.__envpath)     
        self.__logger = Log()

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
            self.__logger.add_info("Key generated")

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
            self.__logger.add_info("Master key generated")
        else:
            print("Master key already exists")
            self.__logger.add_warning("Master key already exists")
    
    def check_master_password(self, password):
        """ function to check if master password is the same as master hash 
        :param password: master password for the program
        :return: true if master password else false
        """
        hash = os.getenv('MASTER')
        ps_hash = hashlib.sha256(password.encode()).hexdigest()
        if ps_hash == hash:
            return True
        else:
            return False
    
    def clear_dotenv(self):
        """ function to clear dotenv file (Testing only)
        :param:
        :return: 
        """
        try:
            os.unsetenv("KEY")
            os.unsetenv("MASTER")
            unset_key(self.__envpath, 'KEY')
            unset_key(self.__envpath, 'MASTER')
            print('Dotenv cleared')
            self.__logger.add_info("Dotenv cleared")
        except Exception as e:
            print(e)
            self.__logger.add_error(e)
    
    def get_key(self):
        """ Get key from dotenv file
        :param:
        :return: master key
        """
        if self.check_key():
            key = bytes(os.getenv('KEY'), 'utf-8')
            self.__logger.add_info("returning master key")
            return key
        else:
            self.__logger.add_error("key not found in dotenv")
            return None
    
    def encrypt(self, data):
        """ function to encrypt data
        :param data: data to encrypt
        :return: encrypted data
        """
        key = self.get_key()
        if key is not None:
            fernet = Fernet(key)
            encode_text = data.encode()
            encrypt_text = fernet.encrypt(encode_text)
            self.__logger.add_info("return encrypted text")
            return encrypt_text
        else:
            self.__logger.add_warning("No key found raised")
            print("No key found")
    
    def decrypt(self, data):
        """ function to decrypt data
        :param data: data to decrypt
        :return: decrypted data
        """
        key = self.get_key()
        if key is not None:
            fernet = Fernet(key)
            decrypt_text = fernet.decrypt(data)
            text = decrypt_text.decode()
            self.__logger.add_info("return decrypted text")
            return text
        else:
            self.__logger.add_warning("No key found raised")
            print("No key found")
        

if __name__ == "__main__":
    c = Crypto()
    c.clear_dotenv()