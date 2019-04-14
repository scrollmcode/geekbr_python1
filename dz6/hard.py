
# Задача - 1
# Вам необходимо создать завод по производству мягких игрушек для детей.
# Вам надо продумать структуру классов,
# чтобы у вас был класс, который создает игрушки на основании:
#  Названия, Цвета, Типа (животное, персонаж мультфильма)
# Опишите процедуры создания игрушки в трех методах:
# -- Закупка сырья, пошив, окраска
# Не усложняйте пусть методы просто выводят текст о том, что делают.
# В итоге ваш класс по производству игрушек должен вернуть объект нового класса Игрушка.

# Задача - 2
# Доработайте нашу фабрику, создайте по одному классу на каждый тип, теперь надо в классе фабрика
# исходя из типа игрушки отдавать конкретный объект класса, который наследуется от базового - Игрушка


class Toy:
    def __init__(self, name, color, toy_type):
        self.name = name
        self.color = color
        self.toy_type = toy_type


class ToyAnimal(Toy):
    pass


class ToyMult(Toy):
    pass


class Zavod:
    def zakupka(self, name):
        print(f"Закупка сырья для {name}.")

    def poshiv(self, name):
        print(f"Пошив {name}.")

    def okraska(self, name):
        print(f"Окраска {name}.")

    def make_toy(self, name, color, toy_type):
        if toy_type == "animal":
            t = ToyAnimal(name, color, toy_type)
        elif toy_type == "mult person":
            t = ToyMult(name, color, toy_type)

        self.zakupka(t.name)
        self.poshiv(t.name)
        self.okraska(t.name)
        return t


toy_types_list = ["animal", "mult person"]

forest_friend_cocporated = Zavod()

toy1 = forest_friend_cocporated.make_toy("Happy Rabbit", "white", toy_types_list[0])
toy2 = forest_friend_cocporated.make_toy("Donald Duck", "blue-white", toy_types_list[1])

print(toy1.name, toy1.color, toy1.toy_type)
print(toy2.name, toy2.color, toy2.toy_type)
