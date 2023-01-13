# python file which handles database

import sqlite3
from logger import Log

# create database table
create_table = """ CREATE TABLE IF NOT EXISTS psv2 (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    service_name VARCHAR(255) NOT NULL,
    username VARCHAR(255),
    password VARCHAR(255) NOT NULL
);"""

# Database class


class Database:

    def __init__(self):
        """ instance initialization of Database class
        :self.__path: path of the database
        :self.__conn: connection to the database
        """
        self.__logger = Log()
        self.__path = r"psv2.db"
        self.__conn = self.create_connection(self.__path)

        if self.__conn is not None:
            self.create_table(self.__conn, create_table)
        else:
            print("Error! cannot connect to database")
            self.__logger.add_error("Error! cannot connect to database @32-db.py")

    def create_connection(self, path=None):
        """ function create a connection to the database
        :param path: path of the database else default None
        :return: connection to the database
        """
        conn = None
        try:
            conn = sqlite3.connect(path)
            self.__logger.add_info(
                'connection to database successfully created returning connection @43-db.py')
            return conn
        except Exception as e:
            self.__logger.add_error(e)
            print(e)

        return conn

    def create_table(self, conn, query_string):
        """ function create a table
        :param conn: connection to the database
        :param query_string: query string
        :return:
        """
        try:
            cur = conn.cursor()
            cur.execute(query_string)
            self.__logger.add_info('table successfully created @60-db.py')
        except Exception as e:
            self.__logger.add_error(e)
            print(e)

    def insert_data(self, service, uname, ps):
        """ function to insert data to the database
        :param service: service name 
        :param uname: username for service 
        :param ps: password for service
        """
        try:
            cur = self.__conn.cursor()

            insert_query = """ INSERT INTO psv2 (
                service_name, username, password) VALUES (?, ?, ?);
                """

            data_tuple = (service, uname, ps)
            cur.execute(insert_query, data_tuple)
            self.__conn.commit()
            print('Data added to database successfully')
            self.__logger.add_info("data added to database successfully @82-db.py")
        except Exception as e:
            print(e)
            self.__logger.add_error(e)

    def delete_all(self):
        """ function to delete all data in the database
        :param:
        :return:
        """
        try:
            sql_query1 = 'DELETE FROM psv2;'
            sql_query2 = 'UPDATE sqlite_sequence SET SEQ=0 WHERE NAME="psv2";'
            cur = self.__conn.cursor()
            cur.execute(sql_query1)
            cur.execute(sql_query2)
            self.__conn.commit()
            print('All data deleted successfully')
            self.__logger.add_info("All data deleted successfully @100-db.py")
        except Exception as e:
            print(e)
            self.__logger.add_error(e)

    def delete_table(self):
        """ function to delete table
        :param:
        :return:
        """
        try:
            sql_query = 'DROP TABLE IF EXISTS psv2;'
            cur = self.__conn.cursor()
            cur.execute(sql_query)
            self.__conn.commit()
            print('Table deleted successfully')
            self.__logger.add_info("Table deleted successfully @116-db.py")
        except Exception as e:
            print(e)
            self.__logger.add_error(e)

    def get_all_data(self):
        """ function to get all data
        :param:
        :return:
        """
        try:
            sql_query = "SELECT * FROM psv2;"
            cur = self.__conn.cursor()
            cur.execute(sql_query)
            rows = cur.fetchall()
            data = [[data for data in row] for row in rows]
            self.__logger.add_info("All data retrieved successfully @132-db.py")
            return data
        except Exception as e:
            print(e)
            self.__logger.add_error(e)

    def get_data_by_id(self, id):
        """ function to get data by id
        :param id: id of data
        :return:
        """
        try:
            sql_query = 'SELECT * FROM psv2 WHERE id = ?'

            cur = self.__conn.cursor()
            cur.execute(sql_query, (id,))
            data = cur.fetchall()
            self.__logger.add_info('Data retrieved successfully @149-db.py')
            return data
        except Exception as e:
            print('Failed to get data')
            print(e)
            self.__logger.add_error(e)
            return None

    def update_data(self, **kwargs):
        """ function to update data
        :param kwargs: keyword arguments
        :return: 
        """
        try:
            if kwargs['data']:
                update_query = """ UPDATE psv2 SET service_name=?, username=?, password=? WHERE id=?"""
                data_tuple = (kwargs['data'][1], kwargs['data']
                              [2], kwargs['data'][3], kwargs['data'][0])

                cur = self.__conn.cursor()
                cur.execute(update_query, data_tuple)
                self.__conn.commit()
                print("Data updated successfully")
                self.__logger.add_info('Data updated successfully @172-db.py')
        except Exception as e:
            print('Failed to update')
            print(e)
            self.__logger.add_error(e)
            return None

    def delete_by_id(self, **kwargs):
        """ function to delete data by id
        :param kwargs: keyword arguments
        :return:
        """
        try:
            if kwargs['id']:
                delete_by_id = " DELETE FROM psv2 WHERE id=?"

                cur = self.__conn.cursor()
                cur.execute(delete_by_id, (kwargs['id'],))
                self.__conn.commit()
                print('Data deleted successfully')
                self.__logger.add_info('Data deleted successfully @-db.py')
        except Exception as e:
            print('Failed to delete')
            print(e)
            self.__logger.add_error(e)
            return None


if __name__ == '__main__':
    db = Database()
    # db.insert_data('youtube', 'cyrof', 'ps')
    # db.insert_data('google', 'cyrof', 'ps')
    # db.insert_data('pi', 'cyrof', 'ps')
    # print(db.get_data_by_id(1))
    db.delete_all()
