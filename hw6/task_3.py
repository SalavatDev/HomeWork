# 3. Реализовать базовый класс Worker (работник).
# ● определить атрибуты: name, surname, position (должность), income (доход);
# ● последний атрибут должен быть защищённым и ссылаться на словарь, содержащий
# элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
# ● создать класс Position (должность) на базе класса Worker;
# ● в классе Position реализовать методы получения полного имени сотрудника
# (get_full_name) и дохода с учётом премии (get_total_income);
# ● проверить работу примера на реальных данных: создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров.

class Worker:

    def __init__(self, name='', surname='', position='', wage=0.0, bonus=0.0):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": float(wage), "bonus": float(bonus)}


class Position(Worker):

    def __init__(self, name='', surname='', position='', wage=0.0, bonus=0.0):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        print(f'Worker name: {self.name}, surname : {self.surname}, position: {self.position}')

    def get_total_income(self):
        print(f'Total income = {sum(self._income.values()):.2f}')


person = Position('Igor', 'Kovalenko', 'Data Scientist', 120000.75, 30000)
person.get_full_name()
person.get_total_income()
