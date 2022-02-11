
# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

n = input('Enter a number: ')
sum = 0
k = 0

while k < int(n):
    k += 1
    sum += int(n*k)

print(sum)

