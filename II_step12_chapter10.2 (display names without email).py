# Дополните приведенный код, чтобы он вывел имена всех пользователей
# (в алфавитном порядке), у которых нет информации об электронной почте.

# Примечание 1. Ключ email может отсутствовать в словаре.
# Примечание 2. Имена необходимо вывести на одной строке, разделяя символом пробела.

users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
         {'name': 'Helga', 'phone': '555-1618'},
         {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
         {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
         {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
         {'name': 'John', 'phone': '233-421-32', 'email': ''},
         {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
         {'name': 'Alina', 'phone': '+7948-799-2434'},
         {'name': 'Robert', 'phone': '420-2011', 'email': ''},
         {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
         {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
         {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
         {'name': 'Roman', 'phone': '+7459-145-8059'},
         {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
         {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
         {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]

# Решение 1 try-except
result_list = []
for i in users:
    try:
        if not i['email'] or i['email'] is None:
            result_list.append(i['name'])
    except:
        result_list.append(i['name'])

print(*sorted(result_list))

# Решение 2 list_comprehension (i.keys())
result_list2 = sorted([i['name'] for i in users if 'email' not in i.keys() or i['email'] == ''])
print(*result_list2)

# Решение 3 double cycle key value items()
result_list3 = []
for i in users:
    for k, v in i.items():
        # Если НЕ вызывать ключ -> i['email'], ошибки не будет. Т.о. правильно -> 'email' not in i
        if (k == 'email' and v == '') or 'email' not in i:
            if i['name'] in result_list3:
                continue
            result_list3.append(i['name'])
print(*sorted(result_list3))

#Решение 4 double list_comprehension(cycle) key value items() set()

result_list4 = sorted(list(set([i['name'] for i in users for k, v in i.items() if (k == 'email' and v == '') or 'email' not in i])))
print(*result_list4)
