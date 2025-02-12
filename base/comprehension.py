'================= Comprehension ======================'
# генератор, с помощью которого мы можем создавать последовательность используя цикл for и условия в одну строчку
# 
# результат for переменная in последовательность
# результат for переменная in последовательность if фильтр
# результат if условия 1 else результат 2 for переменная in последовательность 
# результат if условия 1 else результат 2 for переменная in последовательность if фильтр
# 
# comp = (i for i in range(1,6)) # (1,2,3,4,5)
# print(comp)

# list1 = []
# for i in range(1,6):
#     list1.append(i)


# list1 = [i for i in range(1,6)]
# print(list1)

# list1 = [1,2,3,4,5,]
# list2 = [i for i in list1]


# list1 = [1,2,3,4,5,6,7,8,9]
# list2 = ['четное' if i%2==0 else 'не четное' for i in list1]
# print(list2)

# comprehension делится на 3 вида 
# 1. ListCo
# 2.Set
# 3. Dict 


# dict1 = {1:'a',2:'b',3:'c'}
# dict2 = {k:v for v, k in dict1.items()}
# print(dict2)


'======================Comprehension===================='
# генератор, с помощью которого мы можем создавать последовательность используя цикл for и условия в одну строчку

# результат for переменная in последовательность
# результат for переменная in последовательность if фильтр
# результат1 if условие1 else результат2 for переменная in последовательность
# результат1 if условие1 else результат2 for переменная in последовательность if фильтр

# comp = (i for i in range(1,6)) 
# print(comp)



# list1 = []

# for i in range(1, 6):
#     list1.append(i)

# print(list1)


# list1 = [i for i in range(1,6)]
# print(list1) # [1,2,3,4,5]


# list2 = [32, 4, 13, 4, 1, 12]


# list3 = [i ** 2 for i in list2]
# print(list3)


# list3 = []
# for i in list2:
#     list3.append(i ** 2)
# print(list3)



# list4 = [12, 2, 4, 1, 5, 6, 45, 23, 1]
# list5 = [i for i in list4 if i % 2 == 0]
# print(list5)

# list6 = [12, -23, 32, 2, -4, -3, 0, 0]
# list7 = ['положительное или ноль' if i >= 0 else 'отрицательное' for i in list6]
# print(list7)

# list7 =['положительное или ноль' for i in list6 if i >= 0]
# list8 =['отрицательное' for i in list6 if i < 0]



# 'У вас есть список с числами, Вам нужно созлать новый список вместто четных чисел нужно написать четное в ином случае не четное'

# # list1 = [2, 3, 4] -> ['четное', 'нечетное', 'четное']


# list1 = [1,2,3]
# list2 = ['четное' if i % 2 == 0 else 'нечетное' for i in list1]
# print(list2)


# comprehension делится на 3 вида
# 1. ListComprehension
# 2. SetComprehension
# 3. DictComprehension


# set1 = {i for i in range(11)}
# print(set1)

# list1 = [12, 2, 2, 1, 4, 0.5, 2]

# dict1 = {i:i+10 for i in list1}
# print(dict1)
# # {12:22, 2:12}

# dict2 = {'a':1, "b":2, "c":3}


# dict1 = {1:'a', 2:'b', 3:'c'}
# dict2 = {v: k for k, v in dict1.items()}
# print(dict2)

