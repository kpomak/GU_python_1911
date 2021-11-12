# Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов,
# взятых из трёх списков (по одному из каждого):
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
#
# Например:
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]
#
# Документировать код функции.

from random import choices, sample


def get_jokes(num=1, flag=True):
    """
    Generate jokes in list of items
    :param num: number of jokes (max 5 if flag=False)
    :param flag: prohibits repetitions if False
    :return: None
    """

    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    if flag:
        function_select = choices
    else:
        function_select = sample

    rand_nouns = function_select(nouns, k=num)
    rand_adverbs = function_select(adverbs, k=num)
    rand_adjectives = function_select(adjectives, k=num)

    joke = []

    for noun, adverb, adjective in zip(rand_nouns, rand_adverbs, rand_adjectives):
        joke.append(f'{noun} {adverb} {adjective}')

    print(joke)


get_jokes()
