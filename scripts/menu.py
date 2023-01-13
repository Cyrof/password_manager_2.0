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
            self.__logger.add_info(
                "create master password function running @37-main.py")
            self.create_master()
        else:
            self.__logger.add_info(
                "validate master password function running @41-main.py")
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
                print(colored(
                    "To start, you will have to create a master password. Be careful not to lose it as it is unrecoverable.", 'green'))
                master_ps = getpass.getpass(
                    colored("Create master password for the program: ", 'white'))
                verify_master_ps = getpass.getpass(
                    colored("Verify master password for the program:", 'white'))
                if master_ps == verify_master_ps:
                    self.create_master_password(mps=master_ps)
                    tick = u'\u2713'
                    print(colored(
                        f'{tick} Thank You! Restart the program and enter your master password to begin.', 'green'))
                    self.__logger.add_info(
                        'master password successfully created @71-main.py')
                    break
                else:
                    print(
                        colored("X Password does not match. Please try again X", 'red'))
                    continue
        except KeyboardInterrupt:
            self.__logger.add_info(
                'program terminated by keyboard interrupt @79-main.py')
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
                master_password = getpass.getpass(
                    colored("Enter master password:", 'white'))
                if self.__crypto.check_master_password(master_password):
                    tick = u'\u2713'
                    print(
                        colored(f'{tick} Thank You! Choose an option below...', 'green'))
                    self.__logger.add_info(
                        'Master password successfully validated @106-main.py')
                    break
                else:
                    print(
                        colored("X Master password is incorrect. Please try again X", "red"))
                    self.__logger.add_warning(
                        'Master password is incorrect @112-main.py')
                    continue

        except Exception as e:
            self.__logger.add_error(e)
            print(colored(f'An error occured\n{e}', 'red'))
        except KeyboardInterrupt:
            self.__logger.add_info(
                'program terminated by keyboard interrupt @120-main.py')
            print('Program terminated by keyboard interrupt')
        else:
            self.menu()

    def menu(self):
        """ function to display menu
        :param:
        :return:
        """
        os.system("clear")
        while True:

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
                    self.__logger.add_info(
                        "Store password function running @145-main.py")
                    self.store_password()
                    os.system("clear")
                case '2':
                    self.__logger.add_info(
                        "Update password function running @150-main.py")
                    self.update_ps_menu()
                case '3':
                    self.__logger.add_info(
                        "Retrieve password function running @155-main.py")
                    self.get_a_service()
                case '4':
                    self.__logger.add_info(
                        "Delete password function running @159-main.py")
                    self.delete_pass()
                case '5':
                    self.__logger.add_info(
                        "Delete all Password functions running @163-main.py")
                    self.delete_all_pass()
                case '6':
                    self.__logger.add_info(
                        "Delete all data including master password function running @167-main.py")
                    self.delete_all()
                case 'exit':
                    print(colored("\nExiting...", 'magenta'))
                    break
                case _:
                    self.__logger.add_warning(
                        "Unknown command" + str(choice) + " @174-main.py")
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
            print(colored("Service Name {s} {sym}".format(
                s=service, sym=tick if service is not None else "X"), 'cyan'))
            print(colored("Username {u} {sym}".format(
                u=uname, sym=tick if uname is not None else "X"), 'cyan'))
            print(colored("Password {sym}".format(
                sym=tick if ps is not None else "X"), 'cyan'))

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
                        self.__logger.add_info(
                            "Calling ps valid function @218-main.py")
                        valid = self.ps_valid(ps=ps)
                        if valid:
                            break
                        elif valid == "exit":
                            ps = None
                            break
                        else:
                            continue
                except:
                    continue
            else:
                break

        if service is not None and ps is not None and ps.lower() != "exit":
            self.__logger.add_info(
                "Saving password into database @234-main.py")
            self.__database.insert_data(
                service=service, uname=uname, ps=self.__crypto.encrypt(ps))
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
                self.__logger.add_info(
                    "password verification successful @250-main.py")
                return True
            elif verify_ps.lower() == "exit":
                self.__logger.add_info("exiting... @253-main.py")
                return verify_ps
            else:
                self.__logger.add_warning(
                    "password verification failed @257-main.py")
                print(colored("X Password does not match X", 'red'))
                return False

    def get_service(self):
        """ function to get service name
        :param:
        :return: service name
        """
        self.__logger.add_info("Getting service name @266-main.py")
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
        self.__logger.add_info("Getting username @278-main.py")
        uname = input("(Optional) [Enter to continue] Enter username: ")
        return uname

    def get_ps(self):
        """ function to get password
        :param:
        :return: password
        """
        self.__logger.add_info("Getting password @287-main.py")
        ps = getpass.getpass("Enter password: ")
        if ps == "":
            return None
        else:
            return ps

    def check_db(self):
        """ function to check database is not empty
        :param:
        :return bool:
        """
        datas = self.__database.get_all_data()
        self.__logger.add_info("Checking database @300-main.py")
        if datas:
            return True
        else:
            return False

    def display_all_data(self, **kwargs):
        """ function to display all data
        :param kwargs: keyword arguments
        :return:
        """
        if kwargs['data']:
            datas = kwargs['data']
            datas = [data[:-1] for data in datas]
            p_table = PrettyTable()
            p_table.field_names = ["ID", "Service", "Username"]
            p_table.add_rows(datas)
            self.__logger.add_info("Displaying all data @317-main.py")
            print("\n")
            print(p_table)

    def display_a_service(self, *args, **kwargs):
        """ function to display a service
        :param args: arguments
        :param kwargs: keyword arguments
        :return:
        """
        try:
            if kwargs['data']:
                datas = kwargs['data']
                datas = list(datas[0])
                datas[-1] = self.__crypto.decrypt(datas[-1])
                p_table = PrettyTable()
                p_table.field_names = ["ID", "Service", "Username", "Password"]
                p_table.add_rows([datas])
                self.__logger.add_info("Displaying a service @335-main.py")
                print("\n")
                print(p_table)
                return None
        except Exception as e:
            self.__logger.add_error(e)
            print(e)
        else:
            print("not working")
            self.__logger.add_critical("Not working @344-main.py")

        try:
            if kwargs["sd"]:
                p_table = PrettyTable()
                p_table.field_names = ["ID", "Service", "Username", "Password"]
                p_table.add_rows([kwargs["sd"]])
                self.__logger.add_info("Display service @351-main.py")
                print("\n")
                print(p_table)
                return None
        except Exception as e:
            self.__logger.add_error(e)
            print(e)
        else:
            print("Not working")
            self.__logger.add_critical("Not working @360-main.py")

        return None

    def update_ps(self, **kwargs):
        """ fucntion to update
        :param kwargs: keyword arguments 
        :return:
        """
        if kwargs['data']:
            datas = kwargs["data"]
            datas = list(datas[0])
            service = datas[1]
            uname = datas[2]
            ps = datas[3]

        if kwargs['choice']:
            os.system("clear")
            self.display_a_service(
                data=self.__database.get_data_by_id(kwargs['choice']))

        while True:
            print(colored("\n\t*Enter 'exit' at any point to exit.*", 'magenta'))
            print("1) Service Name")
            print("2) Username")
            print("3) Password")
            print("4) Confirm to update")
            try:
                choice = input("Enter a choice: ")
            except:
                self.__logger.add_error(
                    "Error occured in update ps function @391-main.py")
                print(colored("An error occured. Please try again", 'red'))
                continue

            match choice:
                case '1':
                    service = input("Enter service name to change: ")
                    time.sleep(1)
                    os.system("clear")
                    self.display_a_service(
                        sd=[str(datas[0]), service, uname, self.__crypto.decrypt(ps)])
                    continue
                case '2':
                    uname = input("Enter username to change: ")
                    time.sleep(1)
                    os.system("clear")
                    self.display_a_service(
                        sd=[str(datas[0]), service, uname, self.__crypto.decrypt(ps)])
                    continue
                case '3':
                    ps = input("Enter password to change: ")
                    ps = self.__crypto.encrypt(ps)
                    time.sleep(1)
                    os.system("clear")
                    self.display_a_service(
                        sd=[str(datas[0]), service, uname, self.__crypto.decrypt(ps)])

                    continue
                case '4':
                    datas = [datas[0], service, uname, ps]
                    self.__logger.add_info("updating service @421-main.py")
                    self.__database.update_data(data=datas)
                    break
                case 'exit':
                    print(colored("Exiting...", 'magenta'))
                    self.__logger.add_info(
                        "Exiting update ps function @427-main.py")
                    break
                case _:
                    self.__logger.add_warning(
                        "Unknown command at update ps function @431-main.py")
                    print(colored("X Command not recognized X", 'red'))

    def update_ps_menu(self):
        """ function to update password menu 
        :param:
        :return:
        """
        if self.check_db():
            while True:
                print(colored("\n\t*Enter 'exit' at any point to exit.*", 'magenta'))
                self.display_all_data(data=self.__database.get_all_data())
                try:
                    choice = input("Enter ID of service to update: ")
                    if choice.lower() == "exit":
                        break
                    if choice.isdigit():
                        self.__logger.add_info(
                            "Call update ps function @449-main.py")
                        self.update_ps(data=self.__database.get_data_by_id(
                            int(choice)), choice=choice)
                except:
                    continue
        else:
            self.__logger.add_warning("No data in database")
            print(colored("\nError no data in database", 'red'))

    def get_a_service(self):
        """ retrieve service data
        :param:
        :return:
        """
        if self.check_db():
            while True:
                print(colored("\n\t*Enter 'exit' at any point to exit.*", 'magenta'))
                self.display_all_data(data=self.__database.get_all_data())
                try:
                    choice = input("Enter ID of service to get password: ")
                    if choice.lower() == "exit":
                        break
                    if choice.isdigit():
                        self.display_a_service(
                            data=self.__database.get_data_by_id(int(choice)))
                        break
                except:
                    continue
        else:
            self.__logger.add_warning("No data in database @478-main.py")
            print(colored("\nError no data in database", 'red'))

    def delete_pass(self):
        """ delete password from database
        :param:
        :return:
        """
        if self.check_db():
            while True:
                print(colored("\n\t*Enter 'exit' at any point to exit.*", 'magenta'))
                self.display_all_data(data=self.__database.get_all_data())
                try:
                    choice = input("Enter ID of service to delete password: ")
                    if choice.lower() == "exit":
                        break
                    if choice.isdigit():
                        try:
                            self.__database.delete_by_id(id=int(choice))
                        except Exception as e:
                            self.__logger.add_error(e)
                            print("An error occurred", e)
                        break
                except:
                    continue
        else:
            self.__logger.add_error("No data in database @504-main.py")
            print(colored("\nError no data in database", 'red'))

    def delete_all_pass(self):
        """ delete all data from database
        :param:
        :return:
        """
        if self.check_db():
            choice = input(
                colored("\nAre you sure you want to delete all password datas? [y/n]: ", 'red'))
            if choice.lower() == "y":
                self.__logger.add_info(
                    "Deleting all data from database @517-main.py")
                self.__database.delete_all()
            if choice.lower() == "n":
                pass
        else:
            self.__logger.add_error("No data in database @522-main.py")
            print(colored("\nError no data in database", 'red'))

    def delete_all(self):
        """ Clear entire program data
        :param:
        :return:
        """
        print(colored("\nThis cannot be undone", 'red'))
        choice = input(colored(
            "Are you sure you want to delete all data including master password? [y/n]: ", 'red'))
        if choice.lower() == "y":
            self.__database.delete_all()
            self.__crypto.clear_dotenv()
            print(colored("\nThank you for using our services. Goodbye", 'magenta'))
            self.__logger.add_info(
                "Cleared all data from program @538-main.py")
            exit()
        if choice.lower() == "n":
            pass


if __name__ == '__main__':
    main = Menu()
    # main.welcome_message()
    main.run()
