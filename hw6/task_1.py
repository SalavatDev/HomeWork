# 1. Создать класс TrafficLight (светофор).
# ● определить у него один атрибут color (цвет) и метод running (запуск);
# ● атрибут реализовать как приватный;
# ● в рамках метода реализовать переключение светофора в режимы: красный, жёлтый,
# зелёный;
# ● продолжительность первого состояния (красный) составляет 7 секунд, второго
# (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
# ● переключение между режимами должно осуществляться только в указанном порядке
# (красный, жёлтый, зелёный);
# ● проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении
# выводить соответствующее сообщение и завершать скрипт.

from time import sleep


class TrafficLight:
    __default_colors_time = {'Красный': 7, 'Желтый': 2, 'Зеленый': 5}

    def __init__(self, **kwargs):
        self.__traffic_light = TrafficLight.__default_colors_time.copy()
        if len(kwargs):
            for k, v in kwargs.items():
                if k not in TrafficLight.__default_colors_time.keys():
                    print(f"Params should be one of this: {TrafficLight.__default_colors_time.keys()}")
                    exit()
                if v <= 0:
                    print('The number must be positive and greater than zero!')
                    exit()
                self.__traffic_light[k] = v

    def running(self):
        for k, v in self.__traffic_light.items():
            print(k)
            sleep(v)


svet1 = TrafficLight(Красный=5)
svet1.running()

svet2 = TrafficLight(Красный=7, Желтый=3, Зеленый=7)
svet2.running()
