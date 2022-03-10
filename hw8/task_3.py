# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на
# наличие только чисел. Проверить работу исключения на реальном примере. Запрашивать у
# пользователя данные и заполнять список необходимо только числами. Класс-исключение
# должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока
# пользователь сам не остановит работу скрипта, введя, например, команду «stop». При этом
# скрипт завершается, сформированный список с числами выводится на экран.
# Подсказка: для этого задания примем, что пользователь может вводить только числа и строки.
# Во время ввода пользователем очередного элемента необходимо реализовать проверку типа
# элемента. Вносить его в список, только если введено число. Класс-исключение должен не
# позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение.
# При этом работа скрипта не должна завершаться.

class ControlEnterNumber(Exception):
    def __init__(self, txt):
        self.txt = txt

    @staticmethod
    def is_number_or_str(in_str=''):
        if in_str == '':
            return False
        temp_str = in_str.strip()
        for el in temp_str[1:] if (temp_str.find('-') != -1) else temp_str[:]:
            if not el.isdigit():
                return False
        return True


my_str = input('Enter number or stop for exit: ').lower()
result_list = []
while my_str != 'stop':
    try:
        if not ControlEnterNumber.is_number_or_str(my_str):
            raise ControlEnterNumber('The string must be a number!')
        else:
            result_list.append(int(my_str))

    except ControlEnterNumber as err:
        print(err)

    finally:
        my_str = input('Enter number or stop for exit: ').lower()

print(result_list)
