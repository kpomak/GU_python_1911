"""
Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные
значения функции и выбрасывать исключение ValueError, если что-то не так, например:
def val_checker...
...
@val_checker(lambda x: x > 0)
def calc_cube(x):
return x ** 3
a = calc_cube(5)
125
a = calc_cube(-5)
Traceback (most recent call last):
...
raise ValueError(msg)
ValueError: wrong val -5
"""


from functools import wraps


def val_checker(check_func):
    def _val_checker(func):
        @wraps(func)
        def wrapper(x):
            if check_func(x):
                return func(x)
            else:
                raise ValueError(f'wrong val {x}')
        return wrapper
    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


print(calc_cube(5))
print(calc_cube.__name__)
print(calc_cube(-5))
