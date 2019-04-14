

# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)

# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.


class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go():
        print("Car start go.")

    def stop():
        print("Car stop.")

    def turn(direction):
        print(f"Car turn {direction}")


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


tc1 = TownCar(80, "White", "T1")
sc1 = SportCar(210, "yellow", "s1")
wc1 = WorkCar(100, "Black", "b1")
pc1 = PoliceCar(150, "Blue", "p1")

print(tc1.name, tc1.speed, tc1.color, tc1.is_police)
print(sc1.name, sc1.speed, sc1.color, sc1.is_police)
print(wc1.name, wc1.speed, wc1.color, wc1.is_police)
print(pc1.name, pc1.speed, pc1.color, pc1.is_police)
