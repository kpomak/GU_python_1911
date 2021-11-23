# Добавить возможность редактирования данных при помощи отдельного скрипта:
# передаём ему номер записи и новое значение.При этом файл не должен читаться целиком —
# обязательное требование.Предусмотреть ситуацию, когда пользователь вводит номер записи,
# которой не существует.

import sys
from itertools import islice

program, *args = sys.argv
str_num, value, count = int(args[0]) - 1, args[1], 0

with open('bakery.csv', encoding='utf-8') as f:
    for line in f:
        count += 1

if int(args[0]) > count:
    print("Нет такой записи, братан!")
else:
    with open('bakery.csv', encoding='utf-8') as f:
        with open('temp.txt', 'w', encoding='utf-8') as t:
            for line in islice(f, 0, str_num):
                t.write(line)
            t.write(value + '\n')
            for line in islice(f, 1, None):
                t.write(line)

    with open('temp.txt', encoding='utf-8') as t:
        with open('bakery.csv', 'w', encoding='utf-8') as f:
            for line in t:
                f.write(line)
