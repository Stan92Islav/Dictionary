# На вход программе подается строка, содержащая строки-идентификаторы. Напишите программу, которая исправляет их так,
# чтобы в результирующей строке не было дубликатов. Для этого необходимо прибавлять к повторяющимся идентификаторам
# постфикс _n, где n – количество раз, сколько такой идентификатор уже встречался.

# Формат входных данных
# На вход программе подается строка текста, содержащая строки-идентификаторы, разделенные символом пробела.

# Формат выходных данных
# Программа должна вывести исправленную строку, не содержащую дубликатов сохранив при этом исходный порядок.

s = 'a b c a a d c'.split()

# Решение №1 setdefault
result, d = [], {}

for i in s:
    d.setdefault(i, -1)
    d[i] += 1
    if d[i] >= 1:
        result.append('%s_%d' % (i, d[i]))
    else:
        result.append(i)

print(*result)


# Решение №2 get
result2, d = [], {}

for i in s:
    if i not in result2:
        result2.append(i)
    else:
        d[i] = d.get(i, 0) + 1
        result2.append(i + '_' + str(d[i]))

print(*result2)



# Номер теста	 Входные данные	                            Выходные данные
# 1	             a b c a a d c                              a b c a_1 a_2 d c_1
# 2	             a b c                                      a b c
# 3	             i am i r o n m a n                         i am i_1 r o n m a n_1
# 4	             a a a a a                                  a a_1 a_2 a_3 a_4
# 5	             ab ba a ab                                 ab ba a ab_1
# 6	             let1 ch num num1 x num let1                let1 ch num num1 x num_1 let1_1
# 7	             u u                                        u u_1
# 8	             q w e r t y                                q w e r t y
# 9	             total                                      total
# 10             a a a a a a a aa a a a a a aa a a!         a a_1 a_2 a_3 a_4 a_5 a_6 aa a_7 a_8
#                b b2 b4 b3 a4 a9 a1 a a!                   a_9 a_10 a_11 aa_1 a_12 a! b b2 b4 b3 a4 a9 a1 a_13 a!_1
# 11             name age x x2 j k l name x y k j e a       name age x x2 j k l name_1 x_1
#                x name number                              y k_1 j_1 e a x_2 name_2 number
