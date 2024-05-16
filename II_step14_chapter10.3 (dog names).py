# Вам доступен список pets, содержащий информацию о собаках и их владельцах.  Каждый элемент списка – это кортеж вида
# (кличка собаки, имя владельца, фамилия владельца, возраст владельца).

# Дополните приведенный код так, чтобы в переменной result хранился словарь, в котором для каждого владельца будут
# перечислены его собаки. Ключом словаря должен быть кортеж (имя, фамилия, возраст владельца), а значением – список кличек
# собак (сохранив исходный порядок следования).

# Примечание 1. Не забывайте: кортежи являются неизменяемыми, поэтому могут быть ключами словаря.

# Примечание 2. Обратите внимание, что у некоторых владельцев по несколько собак.

pets = [('Hatiko', 'Parker', 'Wilson', 50),
        ('Rusty', 'Josh', 'King', 25),
        ('Fido', 'John', 'Smith', 28),
        ('Butch', 'Jake', 'Smirnoff', 18),
        ('Odi', 'Emma', 'Wright', 18),
        ('Balto', 'Josh', 'King', 25),
        ('Barry', 'Josh', 'King', 25),
        ('Snape', 'Hannah', 'Taylor', 40),
        ('Horry', 'Martha', 'Robinson', 73),
        ('Giro', 'Alex', 'Martinez', 65),
        ('Zooma', 'Simon', 'Nevel', 32),
        ('Lassie', 'Josh', 'King', 25),
        ('Chase', 'Martha', 'Robinson', 73),
        ('Ace', 'Martha', 'Williams', 38),
        ('Rocky', 'Simon', 'Nevel', 32)]


# Решение №1 setdefault
result = {}
for v, *k in pets:
        result.setdefault(tuple(k), []).append(v)
print(result)

# Решение №2 setdefault
result2 = {}
for i in pets:
        result2.setdefault(i[1:], []).append(i[0])
print(result2)

# Решение3 get
result3 = {}
for i in pets:
        result3[i[1:]] = result3.get(i[1:], []) + [i[0]]

print(result3)

# Решение4 get
result4 = {}
for pet, first_name, second_name, age in pets:
    owner = (first_name, second_name, age)

    result4[owner] = result4.get(owner, []) + [pet]

print(result4)

# Решение №5 defaultdict
from collections import defaultdict
result5 = defaultdict(list)
for i in pets:
        result5[i[1:]].append(i[0])

print(dict(result5))