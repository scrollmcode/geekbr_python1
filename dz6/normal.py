
# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.

import random


class Person:
    def __init__(self, name, health, damage, armor):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor

    def atack(self, enemy_atack):
        enemy_atack.get_damage(self.damage)

    def get_damage(self, damage):
        self.health = self._use_armor(damage)

    def _use_armor(self, damage):
        return self.health - (damage - self.armor)


class Player(Person):
    pass


class Enemy(Person):
    pass


class Game:
    def __init__(self, player1, player2):
            self.player1 = player1
            self.player2 = player2

    def start(self):
        while True:
            self.player1.atack(self.player2)
            end_game = self.health_lost()
            if end_game:
                print(end_game)
                break
            self.player2.atack(self.player1)
            end_game = self.health_lost()
            if end_game:
                print(end_game)
                break

    def health_lost(self):
        if self.player1.health <= 0:
            p2n = selfp.layer2.name
            p2h = round(self.player2.health, 2)
            return (f"Победил {p2n}, осталось {p2h} здоровья.")
        elif self.player2.health <= 0:
            p1n = self.player1.name
            p1h = round(self.player1.health, 2)
            return (f"Победил {p1n}, осталось {p1h} здоровья.")
        else:
            return 0

hero = Player("Hero", 100, 30, 10)
evil_knight = Enemy("Sauron", 100, 30, 10)
Players = [hero, evil_knight]


def select_player():
    index = random.randint(0, 1)
    first_player = Players[index]
    Players.remove(first_player)
    return first_player

print(hero.health)
print(evil_knight.health)
print("\n")

g = Game(select_player(), Players[0])
g.start()

print(hero.health)
print(evil_knight.health)
