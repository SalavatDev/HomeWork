
# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

num = int(input('Enter a number: '))

temp = num // 10
ost = num % 10
m = ost

while temp > 0:
    ost = temp % 10
    temp = temp // 10
    if m < ost:
        m = ost

print(m)



