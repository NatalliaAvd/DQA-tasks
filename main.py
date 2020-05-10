import os
import shutil
from Connector import Connector
from Processor import Processor
#import logger

#работа с файлами
def open_file():
    stroka = ''
    table_name=''
    file_list = os.listdir(path='C:/Users/Natallia_Kavalenka1/input')
    for i in file_list:
        file_path = 'C:/Users/Natallia_Kavalenka1/input/{}'.format(i)
        new_path = 'C:/Users/Natallia_Kavalenka1/incorrect_input'
        if i.endswith('.fb2'):
            with open(file_path, encoding='utf8') as file_content:
                for line in file_content:
                    stroka += str(line)
            table_name = i[:-4:]
            #shutil.move(file_path, new_path)
            i = file_list[-1]
        else:
            shutil.move(file_path, new_path)
    return stroka, table_name


text, table_name = open_file()
#текст с тегами, имя таблицы
if text and table_name:

    work_text = Processor(text)
    book, paragraph = work_text.book_title()

    clear_text = work_text.transform_to_text()#text
    clear_text1=clear_text.split()  # разбиваем строку по словам
    # количество слов
    count_words, big_word, small = work_text.big_letter()#text1


    table1_results = [book, paragraph, count_words, work_text.count_letters(), big_word, small]
    print(table1_results)

    table2_results = work_text.additional_statistics()#text1

    # создание и заполнение таблиц
    if os.path.isfile('C:/PycharmProjects/read_files/library.db'):

        connection_db = Connector(table_name, table1_results, table2_results)

        connection_db.addition_table()
        connection_db.insert_into_statistics_details()
        # conn.commit()
        

    else:
        print("2")
        connection_db = Connector(table_name, table1_results, table2_results)
        
        connection_db.cteation()
        connection_db.insert_into_statistics()

        connection_db.addition_table()
        connection_db.insert_into_statistics_details()




""" 
    print('Название книги:', work_text.book_title())
    print('Количество обзацев в книге:', text.count('<p>'))
    print('Длина строки:', len(clear_text))

    print('Количество слов в тексте:', len(clear_text1))
    print('Количество букв в тексте:', work_text.count_letters())
    print('Количество слов, начинающихся с большой буквы:', big_word)
    print('Количество слов, начинающихся с маленькой буквы:', small)
"""