# Дополните приведенный код так, чтобы он объединил содержимое двух словарей dict1 и dict2: если ключ есть в обоих
# словарях, добавьте его в результирующий словарь со значением, равным сумме соответствующих значений из первого и
# второго словаря; если ключ есть только в одном из словарей, добавьте его в результирующий словарь с его текущим
# значением. Результирующий словарь необходимо присвоить переменной result.

dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}

# Решение №1 in
result = {}
for k, v in dict1.items():
    if k not in result:
        result[k] = v

for k, v in dict2.items():
    if k not in result:
        result[k] = v
    else:
        result[k] += v

print(result)

# Решение №2 get
result2 = {}
for k, v in dict1.items():
    result2[k] = result2.get(k, 0) + v

for k, v in dict2.items():
    result2[k] = result2.get(k, 0) + v

print(result2)

# Решение №3 Counter
from collections import Counter
result3 = Counter(dict1) + Counter(dict2)

print(dict(result3))

# Решение №4 dict_comprehension get set
result4 = {i: dict1.get(i, 0) + dict2.get(i, 0) for i in set(dict1.keys() | dict2.keys())}

print(result4)

# Решение №5 Counter update
result5 = Counter(dict1)
result5.update(dict2)
print(dict(result5))





