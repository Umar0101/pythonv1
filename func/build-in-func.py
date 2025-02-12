# '================= Встроенные функции ================='

# # map, filter, reduce, zip, enumerate 

# # zip - соединяет несколько последовательностей (получаем генератор в котором элементы в котором элементы - tuple)

# list1 = [1, 2, 3, 4, 5]
# list2 = ['a', 'b', 'c']    # ориентируется на наименьший 
# list3 = [0.1, 5.5, 10.8, 0.5]

# zipped = zip(list1, list2, list3)

# # print(list(zipped))

# # for i in zipped:
# #     print(i)

# # enumerate - нумерует последовательность (по дефолту с 0) ( тоже получаем генератор)

# enum = enumerate('hello', 30)
# # print(list(enum))

# # for num, elem in enum:
#     # print(num, elem)


# # map - принимает другую функцию и последовательсть (записывает в новую последовательность резултат функции, в которую передаются элементы последовательности)

# list_ = ['1','2','3','4']
# mapped = map(int, list_)
# # print(list(mapped))

# # for i in mapped:
# #     print(i)

# def func_(x):
#     return x**2

# list_1 = [3,1,2,5]
# mapped2 = list(map(func_, list_1))
# print(mapped2)

# mapped = print(list(map(lambda x: x**2, [1,2,3])))

# # filter - возвращает генератор, с элементами, прошедшими фильтрацию (какое - то условие)б принимает функцию и последовательность 

# list4 = ['hello', 'hi','123','3']
# filtered = filter(str.isdigit, list4)
# print(list( filtered))

# print(list(filter(lambda x: x > 0, [23,-3,2,-5,0])))

# reduce - принимает функцию и последовательность, возвращает 1 результат (передаваемая функция должна принимать 2 аргумента)

# from functools import reduce

# print(reduce(lambda x, y: x + y, [1, 2, 3, 4])) # 17


# print(reduce(lambda x, y: x + y, ['hi', 'D', 'A', 'hello'])) # hiDAhello

'-------------------------------------Задачи------------------------------------------'

 # ZIP

list1 = [1,2,3,4]
list2 = ['a', 'b', 'c', 'd']

# Возведите во 2 степень числа из LIst1
# Сделайте строки верхним регистром в list2
# Сделайте dict1 при помощи zip и этих двух листов

# mapped1 = list(map(lambda x: x**2, list1))
# mapped2 = list(map(str.upper, list2))
# dict1 = dict(zip(mapped1,mapped2))
# print(dict1)


# list1 = ['шалаш', 'мам', 'арора', 'машина']
# print(list(filter(lambda x: x == x[ : :-1], list1)))


