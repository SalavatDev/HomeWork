
# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их
# деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на
# ноль.

def my_func_div(var1, var2):
    try:
        return var1 / var2
    except ZeroDivisionError:
        print('Error: division zero!')
        return 0.0


var_1 = int(input('Enter divisible number: '))
var_2 = int(input('Enter the divisor: '))

print(my_func_div(var_1, var_2))

