"""
Реализуйте базовый класс Car:

у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А
также методы: go, stop, turn(direction), которые должны сообщать, что машина
поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую
скорость автомобиля;

для классов TownCar и WorkCar переопределите метод show_speed. При значении
скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о
превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
выведите результат. Вызовите методы и покажите результат.
"""


class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'машина поехала')

    def stop(self):
        print(f'машина остановилась')

    def turn(self, direction):
        print(f'машина повернула {direction}')

    def show_speed(self):
        print(f'текущая скорость {self.speed} mph')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'превышение скорости на {self.speed - 60} mph')
        else:
            print(f'текущая скорость {self.speed} mph')


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'превышение скорости на {self.speed - 40} mph')
        else:
            print(f'текущая скорость {self.speed} mph')


class SportCar(Car):
    pass


class PoliceCar(Car):
    pass


police = PoliceCar(199, 'black', 'Ford', True)
taxi = TownCar(80, "yellow", 'KIA')
caddy = WorkCar(30, 'white', 'chevrolet')
f_1 = SportCar(500, 'red', 'citroen')

police.show_speed()
taxi.show_speed()
caddy.show_speed()

police.go()
taxi.stop()
caddy.turn('направо')

print(police.is_police)
print(f_1.is_police)