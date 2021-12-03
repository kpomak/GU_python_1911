"""
Написать декоратор для логирования типов позиционных аргументов функции, например:
def type_logger...
...
@type_logger
def calc_cube(x):
return x ** 3
a = calc_cube(5)
5: <class 'int'>
Примечание: если аргументов несколько - выводить данные о каждом через запятую; можете
ли вы вывести тип значения функции? Сможете ли решить задачу для именованных
аргументов? Сможете ли вы замаскировать работу декоратора? Сможете ли вывести имя
функции, например, в виде:
a = calc_cube(5)
calc_cube(5: <class 'int'>)
"""
from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper(one, two, three):
        numbers = one, two, three
        for num in numbers:
            end = '\n' if num == three else', '
            print(f'{func.__name__}({num}: {type(num)})', end=end)
        return func(*numbers)
    return wrapper


@type_logger
def calc_cube(one, two, three):
    numbers = one, two, three
    result = [num ** 3 for num in numbers]
    return result


a = calc_cube(3, 2, 6)
print(a)
print(calc_cube.__name__)
