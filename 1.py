# Выяснить тип результата выражений:
# 15 * 3
# 15 / 3
# 15 // 2
# 15 ** 2

a, b, c, d = 15 * 3, 15 / 3, 15 // 2, 15 ** 2
print(f'15 * 3 = {a} {type(a)}\n'   # <class 'int'>
      f'15 / 3 = {b} {type(b)}\n'   # <class 'float'>
      f'15 // 2 = {c} {type(c)}\n'  # <class 'int'>
      f'15 ** 2 = {d} {type(d)}')   # <class 'int'>
