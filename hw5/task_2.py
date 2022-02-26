# 2. Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить
# подсчёт строк и слов в каждой строке.

with open('task2.txt', 'r', encoding='utf-8') as obj_file:
    content = obj_file.readlines()

for i, cnt in enumerate(content, 1):
    print(f'{i} -', len(cnt.split()))
