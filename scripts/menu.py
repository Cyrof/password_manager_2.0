# python file which handles menu for the password manager

from crypto import Cryptography
from db import Database
from logger import Log
import getpass
from pyfiglet import Figlet
from termcolor import colored
from prettytable import PrettyTable
import os
import time

# menu class for the password manager
class Menu:

    def __init__(self):
        """ Instance Initialization for menu class
        :self.__crypto: instance of Crypto class
        :self.__database: instance of Database
        :self.__logger: instance of Logger
        :self.__figlet : instance of figlet
        """
        self.__crypto = Cryptography()
        self.__database = Database()
        self.__logger = Log()
        self.__figlet = Figlet(font='standard')
    
    def run(self, *args, **kwargs):
        """ Run the password manager menu
        :param args: arguments key-value pairs
        :param kwargs: keyword arguments
        """
        if not self.__crypto.check_master():
            self.__logger.add_info("create master password function running")
            self.create_master()
        else:
            self.__logger.add_info("validate master password function running")
            self.validate_master_password()
    
    def welcome_message(self):
        """ function to display welcome message
        :param:
        :return:
        """
        print(colored(self.__figlet.renderText("\nWelcome to PSV2\n"), 'green'))
    
    def create_master(self):
        """ function to create master password
        :param:
        :return:
        """
        self.welcome_message()
        try:
            while True:
                print(colored("To start, you will have to create a master password. Be careful not to lose it as it is unrecoverable.", 'green'))
                master_ps = getpass.getpass(colored("Create master password for the program: ", 'white'))
                verify_master_ps = getpass.getpass(colored("Verify master password for the program:", 'white'))
                if master_ps == verify_master_ps:
                    self.create_master_password(mps=master_ps)
                    tick = u'\u2713'
                    print(colored(f'{tick} Thank You! Restart the program and enter your master password to begin.', 'green'))
                    self.__logger.add_info('master password successfully created')
                    break
                else:
                    print(colored("X Password does not match. Please try again X", 'red'))
                    continue
        except KeyboardInterrupt:
            self.__logger.add_info('program terminated by keyboard interrupt')
            print('Program terminated by keyboard interrupt')
    
    def create_master_password(self, **kwargs):
        """ function to create master password
        :param kwargs: keyword arguments
        :return:
        """
        if kwargs['mps']:
            self.__crypto.generate_master(kwargs['mps'])
            self.__crypto.generate_key()

    def validate_master_password(self):
        """ function to validate master password
        :param:
        :return:
        """
        self.welcome_message()
        try:
            while True:
                master_password = getpass.getpass(colored("Enter master password:", 'white'))
                if self.__crypto.check_master_password(master_password):
                    tick = u'\u2713'
                    print(colored(f'{tick} Thank You! Choose an option below...', 'green'))
                    self.__logger.add_info('Master password successfully validated')
                    break
                else:
                    print(colored("X Master password is incorrect. Please try again X", "red"))
                    self.__logger.add_warning('Master password is incorrect')
                    continue

        except Exception as e:
            self.__logger.add_error(e)
            print(colored(f'An error occured\n{e}', 'red'))
        else:
            self.menu()

    def menu(self):
        """ function to display menu
        :param:
        :return:
        """
        while True:
            os.system("clear")
            print(colored("\n\t*Enter 'exit' at any point to exit.*\n", 'magenta'))
            print(colored("1) Store a password", 'cyan'))
            print(colored("2) Update a password", 'cyan'))
            print(colored("3) Retrieve a password", 'cyan'))
            print(colored("4) Delete a password", 'cyan'))
            print(colored("5) Erase all passwords", 'red'))
            print(colored("6) Delete all data including master password", 'red'))
            choice = input(colored("Enter a choice: ", 'white'))

            match choice:
                case '1':
                    self.__logger.add_info("Store password function running")
                    self.store_password()
                case '2':
                    pass
                case '3':
                    pass
                case '4':
                    pass
                case '5':
                    pass
                case '6':
                    pass
                case 'exit':
                    print(colored("\nExiting...", 'magenta'))
                    break
                case _:
                    self.__logger.add_warning("Unknown command" + str(choice))
                    print(colored("\nX Command not recognized X", 'red'))
                    time.sleep(1)
    
    def store_password(self):
        """ function to store a password to database
        :param:
        :return:
        """
        service = None
        uname = None
        ps = None
        tick = u'\u2713'
        while True:
            os.system('clear')
            print(colored("\n\t*Enter 'exit' at any point to exit.*\n", 'magenta'))
            print(colored("Service Name {s} {sym}".format(s=service, sym=tick if service is not None else "X"), 'cyan'))
            print(colored("Username {u} {sym}".format(u=uname, sym=tick if uname is not None else "X"), 'cyan'))
            print(colored("Password {sym}".format(sym=tick if ps is not None else "X"), 'cyan'))

            if service is None:
                try:
                    service = self.get_service()
                    if service.lower() == "exit":
                        break
                except:
                    continue
            elif uname is None:
                try:
                    uname = self.get_uname()
                    if uname.lower() == "exit":
                        break
                except:
                    continue
            elif ps is None:
                try:
                    ps = self.get_ps()
                    if ps.lower() == "exit":
                        break
                    if ps is not None and ps.lower() != "exit":
                        valid = self.ps_valid(ps=ps)
                        if valid:
                            break
                        elif valid == "exit":
                            ps=None
                            break
                        else:
                            continue
                except:
                    continue
            else:
                break

        if service is not None and ps is not None and ps.lower() != "exit":
            self.__logger.add_info("Saving password into database")
            self.__database.insert_data(service=service, uname=uname, ps=self.__crypto.encrypt(ps))
            print(colored("Saving your password into database...", 'green'))
            time.sleep(2)

    def ps_valid(self, ps=None):
        """ function to validate password
        :param ps: password argument else default none
        :return bool: if password match
        """
        if ps is not None:
            verify_ps = getpass.getpass("Verify password: ")
            if ps == verify_ps:
                print(colored("Thank you for verifying your password", 'green'))
                self.__logger.add_info("password verification successful")
                return True
            elif verify_ps.lower() == "exit":
                self.__logger.add_info("exiting...")
                return verify_ps
            else:
                self.__logger.add_warning("password verification failed")
                print(colored("X Password does not match X", 'red'))
                return False

    
    def get_service(self):
        """ function to get service name
        :param:
        :return: service name
        """
        self.__logger.add_info("Getting service name")
        service = input("Enter service name: ")
        if service == "":
            return None
        else:
            return service
    
    def get_uname(self):
        """ function to get username
        :param:
        :return: username
        """
        self.__logger.add_info("Getting username")
        uname = input("(Optional) [Enter to continue] Enter username: ")
        return uname
    
    def get_ps(self):
        """ function to get password
        :param:
        :return: password
        """
        self.__logger.add_info("Getting password")
        ps = getpass.getpass("Enter password: ")
        if ps == "":
            return None
        else:
            return ps


        


    


if __name__ == '__main__':
    main = Menu()
    # main.welcome_message()
    main.run()