
# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента и
# возвращает сумму наибольших двух аргументов.

def my_func(var1, var2, var3):
    return var1 + var2 + var3 - min(var1, var2, var3)


var1, var2, var3 = tuple(input('Enter three numbers separated by a space: ').strip().split())
print(my_func(int(var1), int(var2), int(var3)))

