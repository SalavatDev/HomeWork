# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем. При вводе нуля в качестве
# делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class Divzero(Exception):

    def __init__(self, txt):
        self.txt = txt


def division_number(a, b):
    try:
        if b == 0:
            raise Divzero("Делить на ноль нельзя!")
        else:
            return a / b
    except Divzero as err:
        return err


num_1 = int(input('Enter divider number: '))
num_2 = int(input('Enter divisible number: '))

print(division_number(num_1, num_2))
