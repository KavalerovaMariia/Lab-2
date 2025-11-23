from csv import reader
from locale import currency


#Вывести количество записей, у которых в поле Название строка длиннее 30 символов.
with open('books.csv', 'r', encoding='windows-1251') as csvfile:
    table = reader(csvfile, delimiter=';')
    i = 0
    for row in table:
        if len(row[1]) > 30:
            i = i + 1
    print(i)
#Реализовать поиск книги по автору, использовать ограничение на выдачу в зависимости от варианта.

with open('books.csv', 'r', encoding='windows-1251') as csvfile:
    table = reader(csvfile, delimiter=';')
    search = input()
    for row in table:
        if search == row[3] and int(row[7]) < 200:
            print(row[1])
        else:
            print("Ничего не найдено")
            break
#Реализовать генератор библиографических ссылок вида <автор>. <название> - <год> для 20 записей.
#Записи выбрать произвольно.
#Список сохраняется как отдельный файл текстового формата с нумерацией строк.
output = open('result.txt', 'w')
with open('books.csv', 'r', encoding='windows-1251') as csvfile:
    table = reader(csvfile, delimiter=';')
    count = 0
    row_number = 0
    for row in table:
        row_number = int(count)
        count+=1
        if row_number > 99 and row_number < 120:
            date = str(row[6])
            year = date[6:10]
            output.write(f'{row_number}. Название:{row[1]}. Автор: {row[3]}. Год:{year}\n')#print(row[1],row[3],row[6])
output.close()
#Используя приложенный файл currency.xml, выполнить следующее:
#Распарсить файл и извлечь данные, согласно варианту. Выполнить приведения типов по необходимости.

import xml.dom.minidom as minidom
xml_file = open('currency.xml', 'r')
xml_data = xml_file.read()
dom = minidom.parseString(xml_data)
dom.normalize()

elements = dom.getElementsByTagName('Valute')
currency_dict = {}

for node in elements:
    for child in node.childNodes:
        if child.nodeType == 1: #1-тип узла в xml(тег)
            if child.tagName == 'NumCode':
                if child.firstChild.nodeType == 3:
                    NumCode = int(child.firstChild.data)
            if child.tagName == 'CharCode':
                if child.firstChild.nodeType == 3: # есть ли текст внутри элемента
                    CharCode = child.firstChild.data
    currency_dict[NumCode] = CharCode

for key in currency_dict.keys():
    print(key, currency_dict[key])


xml_file.close()
#Допзадание:

#Вывести перечень всех тегов без повторений (для books-en.csv - перечень издательств без повторений).

with open('books.csv', 'r', encoding='windows-1251') as csvfile:
    table = reader(csvfile, delimiter=';')
    tags = set() #множество, чтобы без повторов
    for row in table:
        for a in list(str(row[12]).split("#")):
            tags.add(a)
    for i in tags:
        print(i)



