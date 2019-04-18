
"""
== Лото ==
Правила игры в лото.
Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.
Количество бочонков — 90 штук (с цифрами от 1 до 90).
Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------
В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 
Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.
Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.
Пример одного хода:
Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87      
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)
Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.
Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html
"""
import random


class Card:
    def __init__(self):
        self.line1 = list()
        self.line2 = list()
        self.line3 = list()
        self.nums = list()


class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

        self.generate_card(player1)
        self.generate_card(player2)

    def generate_card(self, player):
        def generate_number(num_start, num_end):
            num = random.randint(num_start, num_end)
            return num

        num_start = 1
        num_end = 50
        for _ in range(5):
            num_start = generate_number(num_start, num_end)
            while num_start in player.nums:
                num_start = generate_number(num_start, num_end)

            player.line1.append(num_start)
            player.nums.append(num_start)
            num_start += 1
            num_end += 10

        num_start = 1
        num_end = 50
        for _ in range(5):
            num_start = generate_number(num_start, num_end)
            while num_start in player.nums:
                num_start = generate_number(num_start, num_end)

            player.line2.append(num_start)
            player.nums.append(num_start)
            num_start += 1
            num_end += 10

        num_start = 1
        num_end = 50
        for _ in range(5):
            num_start = generate_number(num_start, num_end)
            while num_start in player.nums:
                num_start = generate_number(num_start, num_end)

            player.line3.append(num_start)
            player.nums.append(num_start)
            num_start += 1
            num_end += 10

    def get_next_number(self):
        return random.randint(1, 90)


p1 = Card()
p2 = Card()

g = Game(p1, p2)

print(g.player1.line1)
print(g.player1.line2)
print(g.player1.line3)
print(g.player1.nums)

print("\n")

print(g.player2.line1)
print(g.player2.line2)
print(g.player2.line3)
print(g.player2.nums)

print(g.get_next_number())
