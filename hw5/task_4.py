# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные. При
# этом английские числительные должны заменяться на русские. Новый блок строк должен
# записываться в новый текстовый файл.

dict_replace = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре',
    'Five': 'Пять',
    'Six': 'Шесть',
    'Seven': 'Семь',
    'Eight': 'Восемь',
    'Nine': 'Девять',
    'Ten': 'Десять'
}

with open('task4.txt', 'r', encoding='utf-8') as obj_file:
    content = obj_file.readlines()

result_str = ''
for el in content:
    result_str += el.replace(el.split()[0], dict_replace[el.split()[0]])

with open('task4_new.txt', 'w', encoding='utf-8') as obj_file:
    obj_file.write(result_str)
