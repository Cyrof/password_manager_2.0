# logger class for logging messages

import logging

class Log:
    """ Class variables for logging
    :LVL: level of logging
    :FILEPATH: location of log file
    :FORMAT: format of log message
    :logging.basicConfig: set basic configuration
    """
    LVL=logging.INFO
    FILEPATH="psv2.log"
    FORMAT="%(asctime)s~%(levelname)s~%(message)s~module:%(module)s"
    logging.basicConfig(level=LVL, filename=FILEPATH, format=FORMAT)

    def __init__(self):
        """ instance initialization function for log class
        """
        self.__logger = logging.getLogger()

    def add_info(self, message):
        """ function to add log message level information
        :param message: log message
        :return:
        """
        self.__logger.info(message)
    
    def add_warning(self, message):
        """ function to add log message level warning
        :param message: log message
        :return:
        """
        self.__logger.warning(message)
    
    def add_error(self, message):
        """ function to add log message level error
        :param message: log message
        :return:
        """
        self.__logger.error(message)

    def add_debug(self, message):
        """ function to add log message level debug
        :param message: log message
        :return:
        """
        self.__logger.debug(message)

    def add_critical(self, message):
        """ function to add log message level critical
        :param message: log message
        :return:
        """
        self.__logger.critical(message)


