'====================== Dict(словари) ==========================='
# dict - изменяемый, итерируемый, 'неупорядоченный', неиндексируемый тип данных, для хранения данных в парах (ключ:значение)

# user = {
#     'name':'Umar',
#     'age':21,
#     'prof':'Dev'
#     }

# print(user['name']) # Umar

# ключами в словаре могут быть только не изменяемые типы данных 
# если в словаре есть одинаковые ключи то сохранится последний 

# dict1 = {'a':1, 'b':2, 'c':3, 'a':4}
# print(dict1) # {'a':4,'b':2,'c':3}

# print(dict1['f']) # KeyError 'f'


'================ Создание =============='

# user = {'a':1, "b":2}
# user = dict([('a',1), ('b',2), ('c',3)])
# user = dict(['ab', 'cd', 'ef']) 
# print(user)

# dict1 = {'prof':'dev'}
# dict1['name'] = 'Umar'
# dict1['age'] = 21
# dict1['prof'] = 'artist'
# print(dict1) # {'prof':'artist', 'name': 'Umar, 'age':21}


'=======================  Методы словаря  ==========================='

# get - это метод который возврящает значение по ключу, если такого ключа нет, то возвращает None или дефолтное значение 

# user = {
#     'name':'Umar',
#     'age':21,
#     'prof':'dev'
# }
# print(user.get('nam')) # None
# print(user.get('nam', 'hi')) # 'hi'


# pop - удаляет пару по ключу и возвращает значение

# user = {
#     'name':'Umar',
#     'age':21,
#     'prof':'dev'
# }

# pop1 = user.pop('age')
# print(pop1)


# popitem - удаляет последнюю пару и возвращает ее ключ и значение

# user = {
#     'name':'Umar',
#     'age':21,
#     'prof':'dev'
# }

# num = user.popitem()
# print(num) # ('prof','dev')



# update - расширяет словарь парами из второго словаря

# dict1 = {1:'a', 2:'b'}
# dict2 = {3:'c', 4:'d'}

# dict1.update(dict2)
# print(dict1)


# fromkeys - метод для создания нового словаря, используя список ключей

# dict1 = dict.fromkeys('hi', 12,)
# print(dict1) # {'h':12, 'i':12}

# dict1 = dict.fromkeys([1,2,3], 12)
# print(dict1) # {'1':12, '2':12, '3':12}




#  user = {1:'a', 2:'b'}
# keys - возвращает все ключи - dict_keys([1,2])
# values - возвращает все значения - dict_values(['a','b'])
# items - возвращает все пары - dict_items ([1,'a'),(2,'b')])



'========================= Итерирование словарей ================================='

# user = {
#     'name':'Umar',
#     'age':21,
#     'prof':'dev'
# }

# for key in user.items():
#     print(key) 


# for key, values in user.items():
#     print(key, values) 



# задание 
# # вам дан словарь 
# dict1 = {'a':1, 'b':2, 'c':3}
# # создайте новый словарь, поменяв ключи со значениями 
# # dict2 = {1:'a',2:'b',3:'c'}

# dict2 = {
#     values: key
#     for key, values in dict1.items()
# }
# print(dict2)

