class Processor():

    def __init__(self, clear_text):
        self.clear_text = clear_text
        self.clear_text1=clear_text.split()  # разбиваем строку по словам

    def count_letters(self):
        # количество букв в тексте
        text = self.clear_text
        punctuation = 0
        for i in text:
            if i.isalpha() is True:
                punctuation += 1
        return punctuation

    def big_letter(self):
        # Количество слов, начинающихся с большой буквы
        text1 = self.clear_text.split()
        bigword = 0
        letter = 0
        for i in text1:
            if i[0] == i[0].upper():
                bigword += 1
            elif i[0].isalpha() is True:
                letter += 1
        return len(text1), bigword, letter

    def additional_statistics(self):
        # считаем статистику для второй таблицы
        #print('start')
        text1 = self.clear_text.split()
        table2 = []
        for i in text1:
            if i[-1].isalpha():
                table2.append((i, text1.count(i), text1.count(i.capitalize())))
            else:
                s = i[-2::]
                table2.append((s, text1.count(s), text1.count(s.capitalize())))
        #print('finish')
        return table2













