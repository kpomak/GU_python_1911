# Решить задачу 4 и реализовать интерфейс командной строки, чтобы можно было
# задать имя обоих исходных файлов и имя выходного файла. Проверить работу скрипта.

import sys

program, *args = sys.argv
users_file, hobbies_file, created_file = args[0], args[1], args[2]
with open(users_file, encoding='utf-8') as u:
    with open(hobbies_file, encoding='utf-8') as h:
        with open(created_file, 'w', encoding='utf-8') as f:
            for line in u:
                hobby = h.readline().strip().replace(',', ', ')
                if not hobby:
                    hobby = 'None'
                f.write(line.strip().replace(',', ' ') + ': ' + hobby + '\n')
            hobby = h.readline()
            if hobby:
                sys.exit(1)

# python3 5.py users.csv hobby.csv users_hobby.txt
