# Реализовать склонение слова «процент» во фразе «N процентов».
# Вывести эту фразу на экран отдельной строкой для каждого из чисел в интервале от 1 до 100.

for count in range(1, 101):
    count = str(count)
    if count[-1] == '1' and count != '11':
        declination = ' '
    elif count[-1] in ('2', '3', '4') and count not in ('12', '13', '14'):
        declination = 'а'
    else:
        declination = 'ов'
    print(count + ' процент' + declination)
