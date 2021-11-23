# Решить задачу 3 для ситуации, когда объём данных в файлах превышает объём
# ОЗУ. Только теперь не нужно создавать словарь с данными. Вместо этого нужно
# сохранить объединенные данные в новый файл (users_hobby.txt). Хобби пишем через
# двоеточие и пробел после ФИО:
# Иванов,Иван,Иванович: скалолазание,охота
# Петров,Петр,Петрович: горные лыжи

from sys import exit

with open('users.csv', encoding='utf-8') as u:
    with open('hobby.csv', encoding='utf-8') as h:
        with open('users_hobby.txt', 'w', encoding='utf-8') as f:
            for line in u:
                hobby = h.readline().strip().replace(',', ', ')
                if not hobby:
                    hobby = 'None'
                f.write(line.strip().replace(',', ' ') + ': ' + hobby + '\n')
            hobby = h.readline()
            if hobby:
                exit(1)

# Smith Jhon: охота, рыбалка
# Петров Петр Петрович: бадминтон, дартс
# Сидоров Сидор Сидорович: пиво, водка
# Андреев Андрей Андреевич: None
