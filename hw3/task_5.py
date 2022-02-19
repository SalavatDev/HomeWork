# 5. Программа запрашивает у пользователя строку чисел, разделённых пробелом. При нажатии
# Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
# разделённых пробелом и снова нажать Enter. Сумма вновь введённых чисел будет
# добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введён после нескольких чисел, то вначале нужно добавить сумму
# этих чисел к полученной ранее сумме и после этого завершить программу


def find_sum(str_var='0'):
    global sum_var
    is_find_stop = False
    ind = str_var.lower().find('stop')
    if ind == -1:
        temp_list = [int(i) for i in str_var.split()]
        sum_var += sum(temp_list)
    else:
        is_find_stop = True
        temp_list = [int(i) for i in str_var[0:ind].split()]
        sum_var += sum(temp_list)
    return is_find_stop


sum_var = 0.0

print('Enter numbers separated by a space, after "stop"-exit, <<enter>>-show sum: ')

is_stop = False

while not is_stop:
    str_var = input().strip()
    is_stop = find_sum(str_var)
    print(sum_var)
