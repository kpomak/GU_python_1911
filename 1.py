# 1. Написать генератор нечётных чисел от 1 до n (включительно),
# используя ключевое слово yield:

def odd_nums(max_num):
    for num in range(1, max_num + 1, 2):
        yield num


nums_gen = odd_nums(int(input('Введите n ')))

print(next(nums_gen))
next(nums_gen)
print(next(nums_gen))

