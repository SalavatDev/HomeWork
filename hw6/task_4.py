# 4. Реализуйте базовый класс Car.
# ● у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А
# также методы: go, stop, turn(direction), которые должны сообщать, что машина
# поехала, остановилась, повернула (куда);
# ● опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# ● добавьте в базовый класс метод show_speed, который должен показывать текущую
# скорость автомобиля;
# ● для классов TownCar и WorkCar переопределите метод show_speed. При значении
# скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о
# превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
# выведите результат. Вызовите методы и покажите результат.

class Car:

    def __init__(self, speed=0, color='', name='', is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Машина {self.name} поехала')

    def stop(self):
        print(f'Машина  {self.name} остановилась')

    def turn(self, direction=''):
        print(f'Машина  {self.name} повернула {direction} ')

    def show_speed(self):
        print(f'Текущая скорость автомобиля равна {self.speed}км/ч')


class TownCar(Car):

    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print(f'Превышение скорости на {self.speed - 60}км/ч')
        else:
            print(f'Текущая скорость автомобиля равна {self.speed}км/ч')


class WorkCar(Car):

    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print(f'Превышение скорости на {self.speed - 40}км/ч')
        else:
            print(f'Текущая скорость автомобиля равна {self.speed}км/ч')


class SportCar(Car):

    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)


class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)


bus1 = TownCar(57, 'Yellow', 'school_bus')
bus1.go()
bus1.show_speed()
bus1.turn('вправо')
bus1.stop()

bus2 = TownCar(70, 'Yellow', 'school_bus')
bus2.go()
bus2.show_speed()
bus2.turn('влево')
bus2.stop()

tractor1 = WorkCar(35, 'Brown', 'Cat')
tractor1.go()
tractor1.show_speed()
tractor1.turn('влево')
tractor1.stop()

tractor2 = WorkCar(47, 'Red', 'Cat')
tractor2.go()
tractor2.show_speed()
tractor2.turn('назад')
tractor2.stop()

car_drift = SportCar(150, 'Белый', 'Honda')
car_drift.go()
car_drift.show_speed()
car_drift.turn('влево')
car_drift.stop()

police = PoliceCar(130, 'Чёрный', 'Linkoln')
police.go()
police.show_speed()
police.turn('правее')
police.stop()
