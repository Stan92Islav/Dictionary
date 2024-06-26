# Набор сообщений.
# На мобильных кнопочных телефонах текстовые сообщения можно отправлять с помощью цифровой
# клавиатуры. Поскольку с каждой клавишей связано несколько букв, для большинства букв
# требуется несколько нажатий клавиш. При однократном нажатии цифры генерируется первый
# символ, указанный для этой клавиши. Нажатие цифры
# 2, 3, 4 или 5 раз генерирует второй, третий, четвертый или пятый символ клавиши.

# 1	.,?!:
# 2	ABC
# 3	DEF
# 4	GHI
# 5	JKL
# 6	MNO
# 7	PQRS
# 8	TUV
# 9	WXYZ
# 0	space (пробел)

# Напишите программу, которая отображает нажатия клавиш, необходимые для введенного сообщения.

# Формат входных данных
# На вход программе подается одна строка – текстовое сообщение.

# Формат выходных данных
# Программа должна вывести нажатия клавиш, необходимых для введенного сообщения.

# Примечание 1. Ваша программа должна обрабатывать как прописные, так и строчные буквы.

# Примечание 2. Ваша программа должна игнорировать любые символы, не указанные в приведенной выше таблице.

# Примечание 3. Nokia 3310, чтобы вспомнить, как это было 😄

d = {
    "1": [".", ",", "?", "!", ":"],
    "2": ["A", "B", "C"],
    "3": ["D", "E", "F"],
    "4": ["G", "H", "I"],
    "5": ["J", "K", "L"],
    "6": ["M", "N", "O"],
    "7": ["P", "Q", "R", "S"],
    "8": ["T", "U", "V"],
    "9": ["W", "X", "Y", "Z"],
    "0": [" "]
}

nums = 'Hello, World!'.upper().replace('"', '')

# Прогоняем во внешнем цикле строку
for i in nums:
    # Прогоняем во внутреннем цикле ключи и значения словаря
    for key, value in d.items():
        # Если такой символ присутсвует в значении, записываем его в список
        if i in value:
            x = list(value)
            # Умножаем ключ на индекс значения и прибавляем один, так как индекс начинается с 0
            print(key * (x.index(i) + 1), end='')

# Sample Input 1:
# Hello, World!
# Sample Output 1:
# 4433555555666110966677755531111

# Sample Input 2:
# He said: "I can solve this problem".
# Sample Output 2:
# 44330777724443111110444022226607777666555888330844444777707777666225553361

# Sample Input 3:
# Bee   Geek!!!
# Sample Output 3:
# 2233330004333355111111111111


