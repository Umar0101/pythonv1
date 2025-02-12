'==================== Exceptions ====================='

# Исключение - это обьекты, которые прерывают работу кода, если они не обработаны 

# Ошибки - обьекты, которые прерывают работу кода, но их нельзя обработать, не считая исключения 

IndexError
# Исключение, которое выходит, когда мы обращаемся по несуществующему индексу 

'''
list1 = [23, 15, 4, 2]
list1[1000]
'IndexError: list index out of range'
'''

'''
list2 = [12, 23, 2, 1]
list2.pop(1000)
IndexError: pop index out of range
'''

'''
list3 = []
list3.pop()
IndexError: pop from empty list
'''

KeyError
# Исключение, которое выходит, когда обращаемся по несуществующему ключу 

'''
dict1 = {'a':1}
dict1['b']
KeyError: 'b'
'''

ValueError
# Когда мы передаем в функцию не корректный для нее тип данных
# Когда мы распаковываем итерируемый обьект на несколько переменных и кол-во переменных не совпадает с кол-вом элементов в итерируемом обьекте

'''
int('10d')
ValueError: invalid literal for int() with base 10: '10d'
'''

'''
a, b, c = 1, 2, 5, 6
ValueError: too many values to unpack (expected 3)
'''

TypeError 
# когда мы пытаемся использовать метод не свойственный какому то типу данных 
# когда мы пытаемся передать функции больше или меньше аргументов, чем принимает функция 

'''
for i in 123456789:
    ...
TypeError: 'int' object is not iterable
'''

'''
5 + '5'
 TypeError: unsupported operand type(s) for +: 'int' and 'str'
'''

'''
'5' + 5 
TypeError: can only concatenate str (not "int") to str
'''

'''
{[1,2,3]:  'hello'}
TypeError: unhashable type: 'list'
'''

'''
input('enter', 2)
TypeError: input expected at most 1 argument, got 2
'''

'''
[].append()
TypeError: list.append() takes exactly one argument (0 given)
'''

ZeroDivisionError
# выходит при делении на 0 

'''
45 / 0
ZeroDivisionError: division by zero
'''

'''
45 // 0
ZeroDivisionError: integer division or modulo by zero
'''

'''
3 % 0
ZeroDivisionError: integer modulo by zero
'''

AttributeError
# выходит, когда мы обращаемся к несуществующему аттрибуту или методу обьекта(типа данных)

'''
[].replace('', 'a')
AttributeError: 'list' object has no attribute 'replace'
'''

'''
''.pop()
AttributeError: 'str' object has no attribute 'pop'
'''

SyntaxError

'''
my name = 56
SyntaxError: invalid syntax
'''

'''
a = 
SyntaxError: invalid syntax
'''

IndentationError
# Исключение, которое выходит, когда мы используем неправильные отступы

'''
     num = 56
IndentationError: unexpected indent
'''

'''
for i in range(11):
print(i)
IndentationError: expected an indented block after 'for' statement on line 135
'''

NameError
# исключение, которое выходит когда мы обращаемся несуществующей переменной

'''
num1 = 15
print(num2)
NameError: name 'num2' is not defined. Did you mean: 'num1'?
'''

Exception
# Исключение, которое создали, чтобы его вызывать 


'===================== Вызов исключении ===================='

# raise NameError('я вызвал неймеррор просто так')

'================ Обработка исключении ================'
# Чтобы код не прекращал свою работу, мы можем использовать конструкцию ry-except, и обрабатывать вызванное исключение

try:
    # код, который возможно вызовет ошибку
    num = int(input('Введите число: '))
except ValueError:
    # код который, отрабатывает только если ошибка вызвалась
    print('Вы ввели не число')
else:
    # код который, отрабатывает только если никакая ошибка не вышла
    print('Вы ввели число')
finally:
    print('До свидания!')



try: 
    raise ValueError
except (AttributeError, ValueError):
    print('Вышла ошибка - AttributeError или ValueError')



try:
    raise ZeroDivisionError
except:
    print('hi')



try:
    raise ZeroDivisionError
except Exception:
    print('hi')


try:
    raise ValueError
except ValueError:
    print('Вышел ValueError')
except TypeError:
    print('Вышел TypeError')