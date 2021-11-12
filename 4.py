# Написать функцию thesaurus_adv(), принимающую в качестве аргументов
# строки в формате «Имя Фамилия» и возвращающую словарь, в котором ключи
# — первые буквы
# фамилий, а значения — словари, реализованные по схеме предыдущего
# задания и содержащие
# записи, в которых фамилия начинается с соответствующей буквы. Например:
# >>> thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев",
# "Илья Иванов", "Анна Савельева")
# {
# "А": {
# "П": ["Петр Алексеев"]
# },
# "И": {
# "И": ["Илья Иванов"]
# },
# "С": {
# "И": ["Иван Сергеев", "Инна Серова"],
# "А": ["Анна Савельева"]
# }
# }
def thesaurus(*args):
    people = {}
    for name in args:
        if name[0] in people:
            people[name[0]].append(name)
        else:
            people[name[0]] = [name]
    return dict(sorted(people.items()))


def thesaurus_adv(*args):
    people = {}
    for name in args:
        if name.split()[-1][0] in people:
            people[name.split()[-1][0]].append(name)
        else:
            people[name.split()[-1][0]] = [name]
    people = dict(sorted(people.items()))

    for letter, person in people.items():
        if len(person) > 1:
            people[letter] = thesaurus(*person)

    for key, value in people.items():
        print(f" '{key}': {value}")


thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Вадим Ипатов", "Анна Савельева")
