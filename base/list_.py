'========================= List(списки) ==========================='

# списки - изменяемый, индексируемый, итерируемый тип данных, предназначенный для хранения любых типов данных в определенном порядке

# list1 = [1, 2, 3, 2.6, 'hi', [3,4,5], True, False, None]
# print(list1[0])
# print(list1[4])
# print(list1[-4])
# print(list1[4])
# print(list1[5][2])

# list2 = list('hello world')
# print(list2)

# print(list(range(1, 10)))

# # range - это функция которая создает последовательность 
# # range(start, end(не включительно), step)

# print(list(range(0, 56, 2)))
#[0, 2, 4, 6, 8] 


'======================== Методы списков ============================='

# append - добавляет элемент в конец списка

# list3 = [9, 10, 'hi']
# list3.append(20)
# print(list3) # [20]
# list3.append('hi')
# print(list3) # [20, 'hi']


# pop - удаляет элемент из списка по индексу и возвращает удаленный элемент, если индекс не указать то удалит последний элемент 

# list4 = ['hi', 'hello', 'katana']count('l')
# print(count_0) 
# list4.pop(-1)
# print(list4)

# list4 = ['hi', 'hello', 'katana']
# x = list4.pop(-1) # можно сохранить удаленный элемент 
# print(list4)
# print(x)


# remove - удаляет элемент из списка по значению (remove - не возвращает удаленный элемент)

# list6 = [44,4,4,5,54,6,67,7,8,8,8,57,8,57,5,74,45,3,53,534,53,654,6]
# list6.remove(53) #
# print(list6)


# list7 = [0,1,2,4,4,5,0,345,66,0,5]
# count_0 = list.count(0)
# print(count_0) # 3 

# list7 = ['hello', 'hello', 'hello']
# count_0 = list.count('l')
# print(count_0) # ошибка 


# index - возвращает интекс первого вхождения принятого элемента 
# list8 = ['hi', True, False, 12, 'hi', 'good', 12,1,4,0,0,1]
# print(list8.index(элемент, start, end))


# insert - добавляет элемент в список по интексу
# list9 = ['hi', 12, True, False, 0]
# list9.insert(1,'hello')
# print(list9)

# extend - добавляет элементы принятого списка в первый список, изменяя его 
# list10 = [1,2,3]
# list11 = [0,0,0]
# list10.append(list11) #[1,2,3,[0,0,0]]
# list10.extend(list11) #[1,2,3,0,0,0]
# list10.extend('str') # [1,2,3,0,0,0,'s','t','r']
# list10.extend(123) # error

# reverse -  изменяет список раставляя его элементы в обратном порядке 
# list12 = [1,2,3,4,5,6,7,8]
# list13 = [1,2,3,4,5,6,[7,8]]
# list13.reverse()
# list12.reverse()
# print(list12)
# print(list13)

# sort - сортирует список, состоящий из элементов одного типа данных 
# list14 = [23,34,1,4,1,0,45,3,56,3,-4]
# list14.sort()
# print(list14)

# list14 = [23,34,1,4,1,0,45,3,56,3,-4]
# list14.sort(reverse=True)
# print(list14) 


# list15 = ['Umar', 'Adilet', 'Sapar', 'Abu', 'Kalygul', 'Alymbek', 'Myrzabek']
# list15.sort()
# print(list15)

# list16 = ['a', 'r', 'g', 'b', 'y', 'e']
# list16.sort()
# print(list16)

# list17 = [1,2,3,4]
# list17.clear()
# print(list17) # []

# str1 = 'hello'
# list18 = [2,23]

# print(len(str1)) # 5
# print(len(list18)) # 2


# a, b = [15, 20] 
# print(a)

# name, age, prof = ['Umar', 21, 'Dev']

# meshok = ['luk', 'kartoshka', 'ogurec', 'pomidor']
# print(meshok[0])
# print(meshok[1])
# print(meshok[2])
# print(meshok[3])

# for ruka in meshok:
#     print(ruka)

list22 = [True, 'hi', 10, False, -5, 0.5, [1,2,3]]
for i in list22:
    print(i)

# итерация - процесс прохождения по элементам последовательности (итерируемого обьекта)


for i in 'hello world':
    print(i.upper()*5)

str1 = 'hello world'
print(str1.split('l'))  # str --. list

# join :
list_ = ['a', 'b', '12', 'c']
print(''.join(list_)) # list --> str

list_ = ['a', 'b', '12', 'c']
print(' '.join(list_))

list_ = ['a', 'b', '12', 'c']
print('*'.join(list_))

list1 = [1,2,3]
list2 = [1,2,3]

print(list1 == list2)
print(list1 is list2)

'инкримент'
count = 0
count += 1