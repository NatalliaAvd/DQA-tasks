import os
import shutil
import parsing
from Connector import Connector
from Processor import Processor
import logger

def open_file():
    logger.log_settings("Open file")
    text_line = ''
    table_name = ''
    paragraph = 0
    book_name = ''
    file_list = os.listdir(path='C:/Users/Natallia_Kavalenka1/input')
    for i in file_list:
        file_path = 'C:/Users/Natallia_Kavalenka1/input/{}'.format(i)
        new_path = 'C:/Users/Natallia_Kavalenka1/incorrect_input'
        try:
            if i.endswith('.fb2'):
                table_name = i[:-4:]
                # get text from xml, book_name, number of paragraph
                text_line, book_name, paragraph = parsing.parsing(file_path)

                shutil.move(file_path, new_path)
                i = file_list[-1]
                logger.log_settings(".fb2-file is found")
        except Exception:
            shutil.move(file_path, new_path)
            logger.log_settings("Structure of file is incorrect")
            print('Structure of file is incorrect')
    return text_line, table_name, book_name, paragraph

# работа с файлами
def open_file1():
    logger.log_settings("Open file")
    text_line = ''
    table_name = ''
    file_list = os.listdir(path='C:/Users/Natallia_Kavalenka1/input')
    for i in file_list:
        file_path = 'C:/Users/Natallia_Kavalenka1/input/{}'.format(i)
        new_path = 'C:/Users/Natallia_Kavalenka1/incorrect_input'
        try:
            if i.endswith('.fb2'):
                with open(file_path, encoding='utf8') as file_content:
                    for line in file_content:
                        text_line += str(line)
                table_name = i[:-4:]
                shutil.move(file_path, new_path)
                i = file_list[-1]
                logger.log_settings(".fb2-file is found")
        except Exception:
            shutil.move(file_path, new_path)
            logger.log_settings("Structure of file is incorrect")
            print('Structure of file is incorrect')
    return text_line, table_name


def main():
    logger.log_settings("Program started")

    text, table_name, book, paragraph = open_file()
    # текст с тегами, имя таблицы
    if text and table_name:
        logger.log_settings("Work with text")
        work_text = Processor(text)
        #book, paragraph = work_text.book_title()

        #clear_text = work_text.transform_to_text()
        clear_text1 = text.split()  # разбиваем строку по словам
        # количество слов
        count_words, big_word, small = work_text.big_letter()
        table1_results = [book, paragraph, count_words, work_text.count_letters(), big_word, small]

        # print(table1_results)

        table2_results = work_text.additional_statistics()

        logger.log_settings("Connection to DB")
        # создание и заполнение таблиц
        if os.path.isfile('C:/PycharmProjects/read_files/library.db'):
            connection_db = Connector()
            connection_db.addition_table(table_name)
            connection_db.insert_into_statistics_details(table_name, table2_results)
        else:
            connection_db = Connector()
            connection_db.cteation(table_name)
            connection_db.insert_into_statistics(table_name, table1_results)
            connection_db.addition_table(table_name)
            connection_db.insert_into_statistics_details(table_name, table2_results)
    logger.log_settings("Done!")

if __name__ == '__main__':
    main()
