# 2) Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная
# сущность (класс) этого проекта — одежда, которая может иметь определенное название. К
# типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют
# параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и
# H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
# (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке
# знания: реализовать абстрактные классы для основных классов проекта, проверить на
# практике работу декоратора @property.


from abc import ABC, abstractmethod


class Clothes(ABC):

    @abstractmethod
    def fabric_consumption(self):
        pass

    @staticmethod
    def total_consumption(list_cloth=[]):
        total_length = 0.0
        for el in list_clothes:
            total_length += el.fabric_consumption
        return round(total_length, 2)


class Suit(Clothes):

    def __init__(self, height):
        self.height = height

    @property
    def fabric_consumption(self):
        return 2 * self.height + 0.3


class Coat(Clothes):

    def __init__(self, size_coat):
        self.size_coat = size_coat

    @property
    def fabric_consumption(self):
        return self.size_coat / 6.5 + 0.5


my_suit_1 = Suit(1.73)
print(f'{my_suit_1.fabric_consumption:.2f}')
my_suit_2 = Suit(1.79)
my_suit_3 = Suit(1.77)

my_coat_1 = Coat(48)
print(f'{my_coat_1.fabric_consumption:.2f}')
my_coat_2 = Coat(47)
my_coat_3 = Coat(50)

list_clothes = [my_suit_3, my_suit_1, my_coat_2]
print(Clothes.total_consumption(list_clothes))
