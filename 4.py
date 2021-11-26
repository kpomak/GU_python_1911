# Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи — верхняя граница
# pазмера файла(пусть будет кратна 10), а значения — общее количество файлов(в том числе и в подпапках), размер
# которых не превышает этой границы, но больше предыдущей(начинаем с 0).
import os


def key_maker(file_name):
    size = 10 ** len(str(os.stat(file_name).st_size))
    return size


file_range, files_stat = 0, {}

for root, dirs, files in os.walk('some_data'):
    for file in files:
        file_range = key_maker(os.path.join(root, file))
        if file_range not in files_stat:
            files_stat.setdefault(file_range, [1, set([os.path.splitext(file)[1][1:]])])
        else:
            files_stat[file_range][0] += 1
            files_stat[file_range][1].add(os.path.splitext(file)[1][1:])

print(files_stat)
# {100000: [902, {'bin'}], 10000: [88, {'', 'bin'}], 1000: [13, {'bin', 'py'}], 10: [5, {'html', 'bin'}]}

files_stat = dict(sorted(files_stat.items()))
files_stat = {key: (value[0], list(value[1])) for key, value in files_stat.items()}

print(files_stat)
# {10: (5, ['bin', 'html']), 1000: (13, ['py', 'bin']), 10000: (88, ['', 'bin']), 100000: (902, ['bin'])}
