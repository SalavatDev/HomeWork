# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А
# также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы —
# конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определите
# параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры,
# уникальные для каждого типа оргтехники.
# 5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём
# оргтехники на склад и передачу в определённое подразделение компании. Для хранения
# данных о наименовании и количестве единиц оргтехники, а также других данных, можно
# использовать любую подходящую структуру (например, словарь).
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых
# пользователем данных. Например, для указания количества принтеров, отправленных на
# склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.

class ValueTypeError(Exception):
    def __init__(self, txt):
        self.txt = txt


class Warehouse:

    def __init__(self, name_warehouse=''):
        self.office_equipment = {'printer': {}, 'scanner': {}, 'xerox': {}}
        self.name_warehouse = name_warehouse

    def __str__(self):
        result_str = f'{self.name_warehouse}\n'
        for k, v in self.office_equipment.items():
            result_str += str(k) + ': {'
            for ki, vi in v.items():
                result_str += str(ki) + ': ' + str(vi) + '; '
            result_str += '} \n'

        return result_str + '\n'

    def take_equipment(self, equipment, count=1):
        try:
            if isinstance(count, int):
                if count < 0:
                    raise ValueTypeError('The number must be positive!')
                else:
                    equip = equipment.get_type_equipment()
                    name_equip = equipment.name_model
                    if equip in self.office_equipment.keys():
                        if name_equip in self.office_equipment[equip].keys():
                            self.office_equipment[equip][name_equip] += count
                        else:
                            self.office_equipment[equip][name_equip] = count

                    else:
                        print('The warehouse does not accept this office equipment!')

            else:
                raise ValueTypeError('The string must be a number!')

        except ValueTypeError as err:
            print(err)

    def give_equipment(self, equipment, count=1):
        try:
            if isinstance(count, int):
                if count < 0:
                    raise ValueTypeError('The number must be positive!')
                else:
                    equip = equipment.get_type_equipment()
                    name_equip = equipment.name_model
                    if equip in self.office_equipment.keys():
                        if name_equip in self.office_equipment[equip].keys():
                            if self.office_equipment[equip][name_equip] > count:
                                self.office_equipment[equip][name_equip] -= count
                            elif self.office_equipment[equip][name_equip] == count:
                                del self.office_equipment[equip][name_equip]
                            else:
                                print('There is not so much office equipment in stock!')

                        else:
                            print(f'Equipment {equip} is not stored in a warehouse!')

                    else:
                        print(f'Equipment {equip} is not stored in a warehouse!')

            else:
                raise ValueTypeError('The string must be a number!')

        except ValueTypeError as err:
            print(err)


class OfficeEquipment:
    formats = ["A2", "A3", "A4", "A5"]

    def __init__(self, name_model='', weight=0.0, price=0.0):
        self.name_model = name_model
        self.weight = weight
        self.price = price


class Printer(OfficeEquipment):
    __type_equipment = 'printer'

    def __init__(self, name_model, weight, price, color=False, max_format='A4'):
        super().__init__(name_model, weight, price)
        self.color = color
        if max_format.upper() in self.formats:
            self.print_format = max_format.upper()
        else:
            print(f'{max_format} is undefined format')

    def print_text(self, text):
        if self.color:
            print(f'The printed text: "{text}" is colored')
        else:
            print(f'The printed text: "{text}" is not colored')

    def get_type_equipment(self):
        return f'{self.__type_equipment}'


class Scanner(OfficeEquipment):
    __type_equipment = 'scanner'

    def __init__(self, name_model, weight, price, color=False, max_format='A4'):
        super().__init__(name_model, weight, price)
        self.color = color
        if max_format.upper() in self.formats:
            self.print_format = max_format.upper()
        else:
            print(f'{max_format} is undefined format')

    def scan_text(self, text):
        if self.color:
            print(f'The scanned text: "{text}" is colored')
        else:
            print(f'The scanned text: "{text}" is not colored')

    def get_type_equipment(self):
        return f'{self.__type_equipment}'


class Xerox(OfficeEquipment):
    __type_equipment = 'xerox'

    def __init__(self, name_model, weight, price, color=False, max_format='A4'):
        super().__init__(name_model, weight, price)
        self.color = color
        if max_format.upper() in self.formats:
            self.print_format = max_format.upper()
        else:
            print(f'{max_format} is undefined format')

    def copy_text(self, text):
        print(f'The text: "{text}" is copied by {self.name_model}')

    def get_type_equipment(self):
        return f'{self.__type_equipment}'


sklad = Warehouse('Warehouse 1')
print_1 = Printer('HP 1200', 3, 15000, True, 'A4')
print_2 = Printer('Panasonic kx-1500mb', 3.5, 19000, True, 'A4')
scaner_1 = Scanner('Sony-j1700', 2, 11000, True, 'A4')
xerox_1 = Xerox('Xerox-s200', 2, 12000, False, 'A4')
xerox_2 = Xerox('HP a9', 3, 9000, False, 'A4')
xerox_3 = Xerox('Fujisu', 2.9, 10790, True, 'A4')

sklad.take_equipment(print_1)
sklad.take_equipment(print_2, 5)
sklad.take_equipment(scaner_1, 4)
sklad.take_equipment(xerox_1, 5)
sklad.take_equipment(xerox_3, 8)
print(sklad)

sklad.give_equipment(xerox_3, 4)
sklad.give_equipment(print_2, 4)
print(sklad)
sklad.give_equipment(print_2, 1)
print(sklad)
