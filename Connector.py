import sqlite3
import os.path
import logger


class Connector():

    def __init__(self):

        self.conn = sqlite3.connect('library.db')
        self.cursor = self.conn.cursor()

    # создание основной таблицы
    def cteation(self, table_name):
        logger.log_settings("Create " + table_name)

        query = """CREATE TABLE {}(
                      book_name text, number_of_paragraph int, number_of_words int,
                      number_of_letters int, words_with_capital_letters int,
                      words_in_lowercase int)""".format(table_name)
        self.cursor.execute(query)

    # создание доп таблицы
    def addition_table(self, table_name):
        table = table_name + '_info'
        logger.log_settings("Create " + table)
        query1 = "CREATE TABLE {}(word text, count int, count_uppercase int)".format(table)

        try:
            self.cursor.execute(query1)
        except sqlite3.OperationalError:
            print('oooops')
            query = "DELETE FROM {}".format(table)
            self.cursor.execute(query)
            self.conn.commit()

    def insert_into_statistics(self, table_name, args):

        logger.log_settings("Insert data into " + table_name)

        query = 'INSERT INTO {} VALUES(?,?,?,?,?,?)'.format(table_name)
        self.cursor.execute(query, args)
        self.conn.commit()

    # insert data into statistics_details table
    def insert_into_statistics_details(self, table_name, args1):

        table = table_name + '_info'

        logger.log_settings("Insert data into " + table)
        query = "INSERT INTO {} VALUES(?,?,?)".format(table)
        self.cursor.executemany(query, args1)
        self.conn.commit()
        self.conn.close()






