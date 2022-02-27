# 6. Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать
# учебный предмет и наличие лекционных, практических и лабораторных занятий по предмету.
# Сюда должно входить и количество занятий. Необязательно, чтобы для каждого предмета
# были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по
# нему. Вывести его на экран.
# Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}


def total_hours(in_str=''):
    pos_l = in_str.find('(л)')
    pos_pr = in_str.find('(пр)')
    pos_lab = in_str.find('(лаб)')
    sum_hours = 0

    # Функция изЪятия числа из строки
    def find_num(pos):
        # pos - позиция, скоторого будем собирать число
        result_hours = 0
        num_str = ''
        while not in_str[pos].isdigit():
            pos -= 1
        while in_str[pos].isdigit():
            num_str += in_str[pos]
            pos -= 1

        result_hours = int(num_str[::-1])
        return result_hours

    # Количество часов лекции
    if pos_l != -1:
        sum_hours += find_num(pos_l)
    # Количество часов практики
    if pos_pr != -1:
        sum_hours += find_num(pos_pr)
    # Количество часов лаб.раб.
    if pos_lab != -1:
        sum_hours += find_num(pos_lab)

    return sum_hours


with open('task6.txt', 'r', encoding='utf-8') as obj_file:
    content = obj_file.readlines()

res_dict = {}

for el in content:
    temp_list = el.split(':')
    res_dict[temp_list[0].strip()] = total_hours(temp_list[1])

print(res_dict)
