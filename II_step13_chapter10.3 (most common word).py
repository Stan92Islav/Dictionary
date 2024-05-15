# Дополните приведенный код, чтобы он вывел наиболее часто встречающееся слово строки s. Если таких слов несколько,
# должно быть выведено то, что меньше в лексикографическом порядке.

s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'

# Решение №1 Counter
from collections import Counter

result = list(sorted(Counter(s.split()).most_common()[:2], key=lambda x: x[0]))[0][0]
print(result)

# Решение №2 get

result2 = {}
for i in s.split():
    result2[i] = result2.get(i, 0) + 1

mx = max(result2.values())

result3 = {}
for key, value in result2.items():
    if value == mx:
        result3[key] = result3.get(key, value)

print(min(result3))


