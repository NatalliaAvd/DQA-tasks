import sqlite3
import os.path

class Connector():

    def __init__(self, table_name, args, args1):
        self.table_name = table_name
        self.args=args
        self.args1=args1
        self.conn = sqlite3.connect('library.db')
        self.cursor = self.conn.cursor()

    # создание основной таблицы
    def cteation(self):
        #global cursor

        query="""CREATE TABLE {}(
                      book_name text, number_of_paragraph int, number_of_words int,
                      number_of_letters int, words_with_capital_letters int,
                      words_in_lowercase int)""".format(self.table_name)
        self.cursor.execute(query)

    #создание доп таблицы
    def addition_table(self):
        table = self.table_name + '_info'
        #query1="SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES"
        query1 = "CREATE TABLE {}(word text, count int, count_uppercase int)".format(table)

        try:
            self.cursor.execute(query1)
        except sqlite3.OperationalError:
            print('oooops')
            query = "DELETE FROM {}".format(table)
            self.cursor.execute(query)
            self.conn.commit()

        """ 
        if self.cursor.execute(query1)==table:
            print(1)
            query="DELETE FROM {}".format(table)
            self.cursor.execute(query)
        else:
            print(2)
            query="CREATE TABLE {}(word text, count int, count_uppercase int)".format(table)
            self.cursor.execute(query)
        """

    def insert_into_statistics(self):
        #global cursor, conn

        query='INSERT INTO {} VALUES(?,?,?,?,?,?)'.format(self.table_name)
        self.cursor.execute(query, self.args)
        self.conn.commit()

    #insert data into statistics_details table
    def insert_into_statistics_details(self):
        #global cursor, conn
        table=self.table_name+'_info'
        query="INSERT INTO {} VALUES(?,?,?)".format(table)
        self.cursor.executemany(query, self.args1)
        self.conn.commit()
        self.conn.close()


"""
# создание таблицы
if os.path.isfile('C:/PycharmProjects/M1/venv/library.db') is False:
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cteation()
    #расконнектить, когда в другом модуле будет реализован механизм генерации имени таблицы
    #addition_table('a3')
    #conn.commit()
else:
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    #addition_table('aiuy')

args1=['book_name1', 2, 3, 4, 5, 6]
insert_into_statistics(args1)
"""





