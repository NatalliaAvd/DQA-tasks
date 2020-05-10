class Processor():

    def __init__(self, stroka):
        self.stroka=stroka
        self.stroka1=stroka.split()  # разбиваем строку по словам

    # определяем заголовок книги
    def book_title(self):
        book_name=''
        title1 = self.stroka.find('<book-title')
        if title1 != -1:
            title2 = self.stroka.find('</book-title>')
            book_name = self.stroka[title1 + len('<book-title>'):title2]
        return book_name, self.stroka.count('<p>')

    #вычищаем теги из текста
    def transform_to_text(self):
        # если в файле есть картинки, то удаляем их

        pict = self.stroka.count('<binary')
        if pict > 0:
            while pict > 0:
                fteg = self.stroka.find('<binary')
                cl_teg = self.stroka.find('</binary>')
                self.stroka = self.stroka[0:fteg] + self.stroka[cl_teg:len(self.stroka)]
                pict -= 1

        # вычищаем текст от тегов
        ans = []
        # state==0 - закрывающийся тег, state==1 - открывающийся тег
        state = 0
        for c in self.stroka:
            if c == '<':
                state = 1
            if c == '>':
                state = 0
            elif state == 0:
                ans.append(c)
        self.stroka = ''.join(ans)
        return self.stroka

    def count_letters(self):
        # количество букв в тексте
        text = self.transform_to_text()
        punctuation = 0
        for i in text:
            if i.isalpha() is True:
                punctuation += 1
        return punctuation

    def big_letter(self):
        # Количество слов, начинающихся с большой буквы
        text1 = self.transform_to_text().split()
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
        print('start')
        text1 = self.transform_to_text().split()
        table2 = []
        for i in text1:
            if i[-1].isalpha():
                table2.append((i, text1.count(i), text1.count(i.capitalize())))
            else:
                s = i[-2::]
                table2.append((s, text1.count(s), text1.count(s.capitalize())))
        print('finish')
        return table2













