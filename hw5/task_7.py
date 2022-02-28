# 7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая
# строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также
# среднюю прибыль. Если фирма получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а
# также словарь со средней прибылью. Если фирма получила убытки, также добавить её в
# словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.

import json

with open('task7.txt', 'r', encoding='utf-8') as obj_file:
    content = obj_file.readlines()

firm_dict = {}
average_dict = {'average_profit': 0.0}
average_profit = 0.0
k = 0

for el in content:
    temp_list = el.split()
    firm_dict[temp_list[0]] = abs(float(temp_list[2]) - float(temp_list[3]))
    if float(temp_list[2]) > float(temp_list[3]):
        average_profit += float(temp_list[2]) - float(temp_list[3])
        k += 1

average_dict['average_profit'] = round(average_profit / k, 2)

result_list = [firm_dict, average_dict]

with open("task7.json", "w", encoding='utf-8') as write_f:
    json.dump(result_list, write_f)
