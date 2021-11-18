# Решить задачу генерации нечётных чисел от 1 до n (включительно),
# не используя ключевое слово yield.

nums_gen = (num for num in range(1, int(input('Введите n ')) + 1, 2))

print(next(nums_gen))
next(nums_gen)
print(next(nums_gen))
