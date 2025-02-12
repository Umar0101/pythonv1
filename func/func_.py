'================== Функции ==================='
# Функции - именнованный блок кода, который может принимать аргументы и возвращать результат 

# def my_sum(x,y): # x,y = параметры
#     return x + y 

# res = my_sum(5, 2) # 5, 2 = аргументы
# print(res)

# res2 = my_sum(10, 23)
# print(res2)



# def my_len(posl):
#     count = 0
#     for i in posl:
#         count += 1
#     return count 

# res1 = my_len([23,4,5,6,3,2]) # 5
# res2 = my_len('hello world') # 11
# res3 = my_len({12,2,23,32,2,12}) # 4 

# hello = 'hello'
# print(my_len(hello)) # 5 



'==================== Виды параметров ======================'

# 1. Обязательные 
# 2. Необязательные
# 3. с дефолтом(со значением по умолчанию)
# 4. *args - все позиционные аргументы, которые не попали в обязательные и с дефолтом
# 5. **kwargs - все лишние именнованные аргументы

# def func_(x,y,z=6):
#     return x + y + z

# func_(10,5)
# func_(10,5,1)

'==================== Виды аргументов ================'

# 1. позиционные (по позиции )
# 2. именнованные ( по названию (параметр=аргумент))

# def add_or_add_10(num1, num2=10):
#     return num1 + num2

# print(add_or_add_10(5,2)) # 7
# print(add_or_add_10(40)) # 50

def func(a,b=10, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)


# func(10)
# func(20,30)
# func(b=30, a=40)
# func(40,50,60,70,80)
# func(40,50,60,70,80,hello='hello world', hi='hi')


'================Lambda===================='
# lambda - анонимная функция, которая записывается в одну строку

# lambda_func = lambda x, y: x ** y
# print(lambda_func(5, 2))


# def func_(x):
#     return x ** 3

'================ Практика ===================='

# 1. Напишите программу на функциях. Вы у пользователя спрашиваете что он хочет сделать 

# 1.Войти
# 2.Зарегистрироваться

# Смотря от того что введет пользователь, вы должны его зарегестрировать или залогинить


# users = [
#     {'username':'katana', 'password1':'205221sula', 'password2':'205221sula'}
#     ]

# Регистрация:
# Вы запрашиваете username, password1, password2
# После того как пользователь введет данные, вам нужно сохранить эти данные в переменную users

# Логин:
# Запросить username, если такой username есть, запросить пароль и проверить правильно ли ввел этот пароль
# Если такого username нет в users то нужно сказать ему такого пользователя нет в базе

users = [
    {'username':'katana', 'password1':'205221sula', 'password2':'205221sula'}
    ]

def menu():
    choice = input('Что вы хотите сделать?\n1.Войти\n2.Зарегестрироваться\n')
    return choice

def register(users):
    username = input('Введите логин: ')
    password1 = input('Введите пароль: ')
    password2 = input('Подтвердите пароль')
    users.append({"username":username, "password1":password1, 'password2':password2})
    print('Вы зарегестрировались')

def login(users):
    username = input('Введите логин: ')
    for user in users:
        if user['username'] == username:
            password = input('Введите пароль: ')
            if password == user['password1']:
                print('Вы успешно вошли')
            else:
                print('Не верный пароль')
            break
    else:
        print('Такого пользователя не существует')



choice = menu()
if choice == '1':
    login(users)
elif choice == '2':
    register(users)




# Напишите калькулятор на функциях. Вы должны запросить у пользователя num1, num2 операции. и вернуть результат

def calculator():
    num1 = float(input('Введите первое число: '))
    operator = input('Введите оператор: ')
    num2 = float(input('Введите второе число: '))
    if operator == '+':
        return('Ответ:',num1 + num2)
    elif operator == '-':
        return('Ответ:',num1 - num2)
    elif operator == '*':
        return('Ответ:',num1 * num2)
    elif operator == '/':
        if num2 == 0:
            return('число нельзя делить на 0') 
        else:    
            return('Ответ:',num1 / num2)
    elif operator == '//':
        return('Ответ:',num1 // num2)
    elif operator == '%':
        if num2 == 0:
            return('число нельзя делить на 0')
        else:  
            return('Ответ:',num1 % num2)
    elif operator == '**':
        return('Ответ:',num1 ** num2)
    else:
        return('Ошибка не верный оператор')

calculator()
    