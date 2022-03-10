# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
# строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с
# декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип
# к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на
# реальных данных.

from calendar import isleap


class Date:
    __isleap_year_dict = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    __norm_year_dict = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    def __init__(self, datatime=None):
        self.datatime = str(datatime)

    def __str__(self):
        return f'Is date: {self.datatime}'

    @classmethod
    def convert_to_date(cls, datatime=None):
        if datatime is not None:
            temp_list = []
            temp_list = datatime.split('-')
            return f'{int(temp_list[0].strip()):02}.{int(temp_list[1].strip()):02}.{int(temp_list[2].strip()):04}'

    @staticmethod
    def valid_datatime(datatime=None):
        if datatime is not None:
            temp_list = [int(el.strip()) for el in datatime.split('-')]
            if (temp_list[1] >= 1) and (temp_list[1] <= 12):
                if temp_list[0] > (
                        Date.__isleap_year_dict[temp_list[1]] if isleap(temp_list[2]) else Date.__norm_year_dict[
                            temp_list[1]]):
                    return False
                else:
                    return True


dt = Date('12 - 05 - 2022')
print(dt)
print(dt.convert_to_date('17-01-1987'))
print(Date.convert_to_date('11-03-2021'))

print(Date.valid_datatime('30 - 02 - 2020'))
print(Date.valid_datatime('29 - 02 - 2020'))
print(Date.valid_datatime('12 - 05 - 2022'))
