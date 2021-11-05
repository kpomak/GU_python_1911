# Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
# можно ли использовать цикл для проверки работы кода сразу для нескольких значений продолжительности,
# будет ли тут полезен список?

duration = [53, -53, 153, 4153, 400153]

for time in duration:
    days = time // 86400
    hours = time % 86400 // 3600
    minutes = time % 3600 // 60
    seconds = time % 60

    if time < 0:
        continue
    elif days:
        print(f'duration = {time}\n{days} дн {hours} час {minutes} мин {seconds} сек')
    elif hours:
        print(f'duration = {time}\n{hours} час {minutes} мин {seconds} сек')
    elif minutes:
        print(f'duration = {time}\n{minutes} мин {seconds} сек')
    else:
        print(f'duration = {time}\n{seconds} сек')
