# Доработать предыдущую функцию в num_translate_adv(): реализовать корректную работу с числительными,
# начинающимися с заглавной буквы — результат тоже должен быть с заглавной. Например:
# >>> num_translate_adv("One")
# "Один"
# >>> num_translate_adv("two")
# "два"

def num_translate_adv(num):
    dictionary = {'zero': 'ноль',
                  'one': 'один',
                  'two': 'два',
                  'three': 'три',
                  'four': 'четыре',
                  'five': 'пять',
                  'six': 'шесть',
                  'seven': 'семь',
                  'eight': 'восемь',
                  'nine': 'девять',
                  'ten': 'десять'}
    capital_letter = False
    if num[0].isupper():
        capital_letter = True
        num = num.casefold()
    if capital_letter and num in dictionary:
        print(f'"{dictionary[num].title()}"')
    elif num in dictionary:
        print(f'"{dictionary[num]}"')
    else:
        print(None)


num_translate_adv('One')
