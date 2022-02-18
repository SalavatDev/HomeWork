
# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента и
# возвращает сумму наибольших двух аргументов.

def my_func(var1, var2, var3):
    return var1 + var2 + var3 - min(var1, var2, var3)


print(my_func(4, 2, 3))

