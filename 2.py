# Создать список, состоящий из кубов нечётных чисел от 1 до 1000
cube_list = []

for number in range(1, 1001, 2):
    cube_list.append(number ** 3)
print(f'Список, состоящий из кубов нечётных чисел от 1 до 1000: {cube_list}')

# Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
# Внимание: использовать только арифметические операции!

result_a = 0

for number in cube_list:
    test_number = 0
    for index, character in enumerate(str(number)):
        test_number += int(character)
    if test_number % 7 == 0:
        result_a += number
print(f'Сумма чисел из этого списка, сумма цифр которых делится нацело на 7 = {result_a}')

# К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка,
# сумма цифр которых делится нацело на 7.

result_b = 0

for index, number in enumerate(cube_list):
    cube_list[index] += 17
    number += 17
    test_number = 0
    for key, character in enumerate(str(number)):
        test_number += int(character)
    if test_number % 7 == 0:
        result_b += number
print(f'Прибавляем 17 к каждому элементу списка, получаем:      {cube_list}')
print(f'Сумма чисел из этого списка, сумма цифр которых делится нацело на 7 = {result_b}')
