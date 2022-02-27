# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых
# пробелами. Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

numbers = [12.1, 0, -18.0, 24.25, 25.89, 1, 2, -1, 11, -99, -35, 6, 14.8, 15]

with open('task5.txt', 'w', encoding='utf-8') as obj_file:
    for el in numbers:
        obj_file.write(str(el) + ' ')

with open('task5.txt', 'r', encoding='utf-8') as obj_file:
    content = obj_file.read().split()

sum_res = 0.0
for el in content:
    sum_res += float(el)

print(f'{sum_res:.2f}')
