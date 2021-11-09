# Дан список:
# ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# Необходимо его обработать — обособить каждое целое число кавычками и
# дополнить нулём до двух целочисленных разрядов

words = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for word in words[:]:
    if word[-1].isdigit():
        words.insert(words.index(word), '"')
        words.insert(words.index(word) + 1, '"')
        if word.isdigit():
            words[words.index(word)] = f'{int(word):02d}'
        else:
            words[words.index(word)] = f'{word[0]}{int(word):02d}'
print(words)

# ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']

# Сформировать из обработанного списка строку:
# в "05" часов "17" минут температура воздуха была "+05" градусов

result = ' '.join(words)
# в " 05 " часов " 17 " минут температура воздуха была " +05 " градусов

open_quote, i = False, 0

while i != len(result):
    if result[i] == '"' and not open_quote:
        result = result[:result.index(result[i], i) + 1] + result[result.index(result[i], i) + 2:]
        open_quote = not open_quote
        i += 1
    elif result[i] == '"' and open_quote:
        result = result[:result.index(result[i], i) - 1] + result[result.index(result[i], i):]
        open_quote = not open_quote
        i += 1
    else:
        i += 1
print(result)

# в "05" часов "17" минут температура воздуха была "+05" градусов
