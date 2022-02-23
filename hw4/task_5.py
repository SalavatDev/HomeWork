from functools import reduce


# 5. Реализовать формирование списка, используя функцию range() и возможности генератора. В список
# должны войти чётные числа от 100 до 1000 (включая границы). Нужно получить результат вычисления
# произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

def func_mult(prev_el, el):
    # prev_el - предыдущий элемент
    # el - текущий элемент
    return prev_el * el


print(reduce(func_mult, [el for el in range(100, 1001) if el % 2 == 0]))
