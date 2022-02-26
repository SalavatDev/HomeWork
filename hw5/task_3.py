# 3. Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и
# величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее
# 20 тысяч, вывести фамилии этих сотрудников. Выполнить подсчёт средней величины дохода
# сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

with open('task3.txt', 'r', encoding='utf-8') as obj_file:
    content = obj_file.readlines()

sal_list = []
sal_average = 0.0
for el in content:
    tmp_list = list(el.split())
    sal_average += float(tmp_list[1])
    if float(tmp_list[1]) < 20000.00:
        sal_list.append(tmp_list[0])

print("Surnames of employees who have a salary less than 20,000:")
for el in sal_list:
    print(el, end=' ')

print('')


print('Average income of all employees: ', round(sal_average / len(content), 2))
