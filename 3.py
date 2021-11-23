# Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.
# Известно, что при хранении данных используется принцип: одна строка — один пользователь,
# разделитель между значениями — запятая. Написать код, загружающий данные из обоих файлов
# и формирующий из них словарь: ключи — ФИО, значения — данные о хобби. Сохранить словарь
# в файл. Проверить сохранённые данные. Если в файле, хранящем данные о хобби, меньше
# записей, чем в файле с ФИО, задаём в словаре значение None. Если наоборот — выходим из
# скрипта с кодом «1». При решении задачи считать, что объём данных в файлах во много раз
# меньше объема ОЗУ.
# Фрагмент файла с данными о пользователях (users.csv):
# Иванов,Иван,Иванович
# Петров,Петр,Петрович
# Фрагмент файла с данными о хобби (hobby.csv):
# скалолазание,охота

import json
from itertools import zip_longest
from sys import exit

with open('users.csv', encoding='utf-8') as u:
    users = u.read().split()
    for i in range(len(users)):
        users[i] = users[i].replace(',', ' ')

with open('hobby.csv', encoding='utf-8') as h:
    hobbies = h.read().split()
    for i in range(len(hobbies)):
        hobbies[i] = hobbies[i].replace(',', ', ')

user_hobbies = {user: hobby for user, hobby in zip_longest(users, hobbies)}
if None in user_hobbies:
    exit(1)

with open('users_hobby.txt', "w", encoding='utf-8') as f:
    json.dump(user_hobbies, f)

with open('users_hobby.txt', encoding='utf-8') as f:
    user_hobbies = json.load(f)

print(user_hobbies)

# {'Smith Jhon': 'охота, рыбалка',
#  'Петров Петр Петрович': 'бадминтон, дартс',
#  'Сидоров Сидор Сидорович': 'пиво, водка',
#  'Андреев Андрей Андреевич': None}
