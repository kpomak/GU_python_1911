# Написать функцию currency_rates(), принимающую в качестве аргумента код
# валюты (например, USD, EUR, GBP, ...) и возвращающую курс этой валюты по
# отношению к рублю. Использовать библиотеку requests. В качестве API можно
# использовать http://www.cbr.ru/scripts/XML_daily.asp. Рекомендация:
# выполнить предварительно запрос к API в обычном браузере, посмотреть
# содержимое ответа. Можно ли, используя только методы класса str, решить
# поставленную задачу? Функция должна возвращать результат числового типа,
# например float. Подумайте: есть ли смысл для работы с денежными величинами
# использовать вместо float тип Decimal? Сильно ли усложняется код функции при
# этом? Если в качестве аргумента передали код валюты, которого нет в ответе,
# вернуть None. Можно ли сделать работу функции не зависящей от того, в каком
# регистре был передан аргумент? В качестве примера выведите курсы доллара и евро.


import requests
from decimal import *
from datetime import date

getcontext().prec = 5
# для метода quantize


def finder(old_string, word):
    new_string = old_string[old_string.find(word) + len(word) + 1:old_string.find('</' + word)]
    return new_string


def currency_rates(currency):
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text.replace(',', '.').split('</Valute>')
    response.pop()

    today = response[0][response[0].find('Date="') + len('Date="'):response[0].find('" name')].split('.')
    today = date(*map(int, today[::-1]))

    exchange = {}
    for money in response:
        currency_value = Decimal(finder(money, "Value")).quantize(Decimal("1.00"), ROUND_HALF_UP)
        exchange[finder(money, 'CharCode')] = ' '.join((finder(money, "Nominal"),
                                                        finder(money, "Name"),
                                                        str(currency_value),
                                                        'руб.,',
                                                        str(today)
                                                        ))
    return exchange.get(currency.upper())


print(currency_rates('GBP'))
print(currency_rates('eur'))
print(currency_rates('usd'))
