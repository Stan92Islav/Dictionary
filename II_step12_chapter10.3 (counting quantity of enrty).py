# Дополните приведенный код так, чтобы в переменной result хранился словарь, в котором для каждого символа строки text
# будет подсчитано количество его вхождений.

text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'

# Решение №1
result = {}
for i in text:
    result[i] = result.get(i, 0) + 1

print(result)

# Решение №2
result2 = {i: text.count(i) for i in set(text)}

print(result2)

# Решение №3
from collections import Counter

result3 = dict(Counter(text))

print(result3)