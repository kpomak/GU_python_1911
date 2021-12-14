"""
== Лото ==
Правила игры в лото.
Игра ведется с помощью спе циальных карточек, на которых отмечены числа,
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
 7 87     - 14    11
      16 49    55 88    77
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html
"""


from random import sample, shuffle


class GameCard:
    def __init__(self, player_name):
        self.name = player_name
        self.body = []

    def card_filling(self):
        raw_list = list(range(1, 91))
        change_list = []
        for i in range(3):
            self.body.append(sample(raw_list, k=9))
            self.body[i].sort()
            for num in self.body[i]:
                raw_list.remove(num)
            change_list.append(sample(self.body[i], k=4))
            self.body[i] = ['  ' if num in change_list[i] else num for num in self.body[i]]

    def replace_number(self, number):
        self.body = [['-' if num == number else num for num in raw] for raw in self.body]

    def check_number(self, number):
        result = False
        for raw in self.body:
            if number in raw:
                result = True
        return result

    def __str__(self):
        face = [list(map(str, num)) for num in self.body]
        face = [(f'{x:>2}' if len(x) < 2 else x for x in char) for char in face]
        return f'{self.name}:\n' \
               f'{"-" * 27}\n' \
               f'{" ".join(face[0])}\n' \
               f'{" ".join(face[1])}\n' \
               f'{" ".join(face[2])}' \
               f'\n{"-" * 27}'


class Game:
    def __init__(self, player, computer):
        self.player = player
        self.computer = computer

    def start(self):
        self.player.card_filling()
        self.computer.card_filling()
        turns_quantity, comp_hit, player_hit = 90, 0, 0
        barrel = list(range(1, 91))
        shuffle(barrel)
        turn = (number for number in barrel)
        while turns_quantity != 0:
            barrel_value = next(turn)
            turns_quantity -= 1
            print('\n' * 15, f'Новый бочонок: {barrel_value} (осталось {turns_quantity})', sep='\n')
            print(self.player, self.computer, sep='\n')
            solution = input('Зачеркнуть цифру (y/n)?\n')
            if self.computer.check_number(barrel_value):
                self.computer.replace_number(barrel_value)
                comp_hit += 1
                if comp_hit == 15:
                    print('Компьютер победил!')
                    break
            if solution == 'y':
                if self.player.check_number(barrel_value):
                    self.player.replace_number(barrel_value)
                    player_hit += 1
                    if player_hit == 15:
                        print('Победа!')
                        break
                else:
                    print('Поражение!')
                    break
            elif solution == 'n':
                if self.player.check_number(barrel_value):
                    print('Поражение!')
                    break
            else:
                print('Непредусмотренный конец игры...')
                break


player_card = GameCard('Игрок')
computer_card = GameCard('Компьютер')

loto_game = Game(player_card, computer_card)
loto_game.start()
