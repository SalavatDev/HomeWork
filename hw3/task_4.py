
# 4. Программа принимает действительное положительное число x и целое отрицательное число
# y. Выполните возведение числа x в степень y. Задание реализуйте в виде функции
# my_func(x, y). При решении задания нужно обойтись без встроенной функции возведения
# числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с
# помощью оператора **. Второй — более сложная реализация без оператора **,
# предусматривающая использование цикла

def my_func1(base, exp):
    return base ** y


def my_func2(base, exp):
    result = 0.0
    if base == 0:
        return 0
    else:
        f = 1
        k = 0
        while k < abs(exp):
            f = f * base
            k += 1
        if exp < 0:
            result = 1 / f

        else:
            result = f
    return result


x = int(input('Enter the base number : '))
y = int(input('Enter the exponent: '))

print(my_func1(x, y))
print(my_func2(x, y))



