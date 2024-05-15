# На вход программе подается строка текста. Напишите программу, которая выводит слово, которое встречается реже всего,
# без учета регистра. Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.

# Формат входных данных
# На вход программе подается строка текста.

# Формат выходных данных
# Программа должна вывести слово (в нижнем регистре), встречаемое реже всего.

# Примечание 1. Программа не должна быть чувствительной к регистру, слова apple и Apple должна воспринимать как одинаковые.

# Примечание 2. Слово — последовательность букв. Кроме слов в тексте могут присутствовать пробелы и знаки препинания
# .,!?:;-, которые нужно игнорировать. Других символов в тексте нет.

s = 'home sweet home sweet.'.lower() # уравниваем регистр

# Решение №1 Counter
from collections import Counter
FiltString = ''.join(filter(lambda x: x.isalpha() or x == ' ', s))  # игнорируем знаки пунктуации
# filt2 = ''.join([i for i in s if i.isalpha() or i == ' ']) # на заметку

count_common = Counter(FiltString.split()).most_common()  # подсчитываем слова, которые будут рассортированы от наиболее к менее повторяющимся
less_common = min([i[1] for i in count_common])           # выбираем наименьший показатель
result = [i for i in less_common if i[1] == less_common]  # добавляем в список только с наименьшим показателем

print(min(result, key=lambda x: x[0])[0])                 # выибраем минимальное слово с т.з. лексиграфического порядка


# Решение №2 dict, get, (key, value, items)
FiltString2 = ''.join(filter(lambda x: x.isalpha() or x == ' ', s)) # игнорируем знаки пунктуации

result2 = {}
for i in FiltString2.split():    # добавляем в словарь result2 слова(ключи) и значения(кол-во)
    result2[i] = result2.get(i, 0) + 1

mn = min(result2.values())       # Находим минимальное значение

result3 = {}
for key, value in result2.items():
    if value == mn:              # добавляем в словарь result3 только ключи с минимальными значениями
        result3[key] = result3.get(key, value)

print(min(result3))              # выбираем минимальный ключ только с т.з. лексиграфического порядка

# Номер теста	                                 Входные данные	                                      Выходные данные
#     1	                                        home sweet home	                                            sweet
#     2	                                      home sweet home sweet.	                                    home
#     3	                                      How are you? how Are?	                                        you
#     4	       London is the capital of Great Britain. More than six million people live in London.         also
#                 London lies on both banks of the river Thames. It is the largest city in Europe and one
#                 of the largest cities in the world. London is not only the capital of the country, it is
#                 also a very big port, one of the greatest commercial centres in the world, a university
#                 city, and the seat of the government of Great Britain!
#     5	        My dear, here we must run as fast as we can, just to stay in place. And if you wish         and
#                 to go anywhere you must run twice as fast as that.
#     6	        I bought two books: a new book and an old book. The new book was more expensive than         a
#                 the old book.
#     7	        наш курс курс самый самый лучший	                                                        лучший