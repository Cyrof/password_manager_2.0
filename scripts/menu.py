# python file which handles menu for the password manager

from crypt import Crypto
from db import Database
import getpass
from pyfiglet import Figlet
from termcolor import colored
from prettytable import PrettyTable

# menu class for the password manager
class Menu:

    def __init__(self):
        """ Instance Initialization for menu class
        :self.__crypto: instance of Crypto class
        :self.__database: instance of Database
        :self.__figlet : instance of figlet
        """
        self.__crypto = Crypto()
        self.__database = Database()
        self.__figlet = Figlet(font='standard')

if __name__ == '__main__':
    c = Crypto()