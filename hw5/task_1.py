# 1. Создать программный файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных будет свидетельствовать пустая
# строка.

with open('task1.txt', 'w', encoding='utf-8') as file_obj:
    content = input('Enter your string or empty string for exit: ')
    while content != '':
        file_obj.write(content + '\n')
        content = input('Enter your string or empty string for exit: ')
