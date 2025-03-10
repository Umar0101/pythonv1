'============== Строки(str) ================'

# Строки - неизменяемый тип данных, который предназначен для хранения текста (последовательности символов), заключенного в одинарные или двойные кавычки 

# string1 = 'строка с одинарными кавычками'

# string2 = "строка с двойными кавычками"

# # error = 'не правильная строка"

# string3 = "Don't"

# string4 = 'Мой никнейм "Legenda"'

# string5 = ''' Привет 

# как
#  дела '''

# string6 = """ Привет 
# как
#  ты"""


# str7 = 'Привет' + 'как дела'  # конкатенация - склеивание строк 
# print(str7)

# str8 = 'Привет' +'       '+ 'как дела'  # конкатенация - склеивание строк 
# print(str8)

# str9 = 'Ha' * 200  # умножение выполняется первым 
# print(str9)

# str10 = ('Ha' +' ') * 200  # умножение выполняется первым 
# print(str10)

'========================== Экранизация =============================='

# '\n' - это перенос на новую строку 
# print('Hello world') # Hello world 
# print('Hello\nworld') # Hello 
#                       # world 

# # '\t' - табуляция 

# print('Hello\tworld') # Hello   world

# print('Don\'t') # Don't 
# print("don\\\"t") # don"t 

# # '\v' - перенос на новую строку со смещением вправо на длинну предыдущей строки 
# print('Hello\vworld\vmetalabs')

# # '\r' - перенос каретки на начало строки 
# print('Hello world\rGo')

'========================== Форматирование строк ==========================='

# title = 'iPhone 16'
# price = 150000
# messege = f'Я купил {title} за {price} сом'
# print(messege)

# messege2 = 'я купил {} за {} сом {}'
# print(messege2.format(title, price, 'очень хорошая покупка')) # через format() можно добавлять и строки(текст)

# messege3 = 'я купил %s за %s сом'
# print(messege3 %(title, price)) # через %() тоже можно добавлять строки(текст)


'========================= Методы строк ==========================='
# Методы - это те же функции, которые относятся к определнному классу (типу данных), к ним мы обращаемся через точку 

# str1 = 'hello world'
# print(str1.upper()) # все будут с большой буквы 
# print('HELLO'.lower()) # все будут с маленькой буквы 
# print('HeLlo'.swapcase()) # hElLO маленькие меняет на большой а большие на маленькие 
# print(str1.capitalize()) # меняет первую букву в предложении на большой 
# print('hello woRlD'.title()) # hello woRlD --> Hello World

# # класс 
# print(dir(str))

# print('hello'.center(11)) # '   hello   '
# print('hello'.center(11, '*')) # '***hello***'

# print('hello world'.count('l')) # 3 считает сколько букв в слове hello 
# print('hello world'.count('ll')) # 1
# print('hello world'.count('lll')) # 0
# print('hello world'.count('hello')) # считает сколько в предложении слово hello 

# print('hello world'.startswith('he')) # true 
# print('hello world'.startswith('H')) # false 

# print('hello world'.endswith('he')) # false
# print('hello world'.endswith('rld')) # true 

# print('hello world'.find(' ')) # ??????????? 

# print('hello world'.islower()) # true
# print('hello world'.islower()) # true

# print('hello world'.isupper()) # false
# print('HELLO WORLD'.isupper()) # true

# print('hello'.isdigit()) # false проверяет полностью ли текст состоит из чисел
# print('34535'.isdigit()) # true проверяет полностью ли текст состоит из чисел

# print('hello'.isalpha()) # true проверяет полностью ли текст состоит из букв 

# print('hello 123'.isalnum()) # false
# print('hello123'.isalnum()) # true
# print('hello'.isalnum()) # true

# print('hello'.isdecimal()) # ?????????

# print('hello world'.replace('e', 'i')) # hello world --> hillo world
# print('hello world'.replace('o', 'i')) # hello world --> helli wirld
# print('hello world'.replace('o', 'i', 1)) # hello world --> helli world

# print('hello world'.split()) # ????
# print('hello world'.join()) # ????? 

'============================== Индексы =================================='

# index - это порядковый номер элемента в последовательности (символа в строке) индексация начинается с 0 
#'h e l l o   w o r l d'
# 0 1 2 3 4 5 6 7 8 9 10
#             ... -2 -1

string = 'hello world'

print(string.join())

# print(string[0])  # h 
# print(string[10]) # d
# print(string[-1]) # d 
# print(string[5]) # 'пробел' ''

# # срез - подстрока строки (часть строки) str[start:end;step]

# print(string[2:5]) # llo
# print(string[0:4]) # hell
# print(string[4:]) # o world 
# print(string[:]) # hello world 
# print(string[ : :2]) # hlowrd
# print(string[ : :-1])  # dlrow olleh 
# print(string[ -5:-1: ]) # worl 
# print(string[-1:-5:-1]) #dlro 

# # print('helo'[:3].replace('')) 

# str10 = 'hello'
# print(str10.replace('h', 'd')) # dello 
# print(str10) # hello










