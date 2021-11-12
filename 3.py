# Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
# в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
# Например:
# >>> thesaurus("Иван", "Мария", "Петр", "Илья")
# {
#     "И": ["Иван", "Илья"],
#     "М": ["Мария"],
#     "П": ["Петр"]
# }

def thesaurus(*args):
    people = {}
    for name in args:
        if name[0] in people:
            people[name[0]].append(name)
        else:
            people[name[0]] = [name]
    people = dict(sorted(people.items()))

    print("{")
    for key, value in people.items():
        print(f'     "{key}": {value}')
    print("}")


thesaurus("Иван", "Мария", "Петр", "Илья")

# {
#      "И": ['Иван', 'Илья']
#      "М": ['Мария']
#      "П": ['Петр']
# }
