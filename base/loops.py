# циклы - это блок кода, который выполняет код определенное (неопределенное) кол-во раз
# for, while

# for - работает до конца итерируемого обьекта

# while - работает пока условие верное (True) если в условии появляется (False) то цикл завершает работу


'FOR' 

# list1 = [1, 2,3, 'hi']

# for i in list1:
#     print(i)

'WHILE'

# count = 0
# while count < 10:
#     print('hi')
#     count += 1

# n = 0 
# while n: # цикл не сработает пока тут False
#     print('hi')

# str1 = input('введите слово: ')
# while str1.islower():
#     print('с маленькой')
#     str1 = str1.upper()
#     print(str1)


'===========================  Break, continue  =============================='

# Break(ломать) = оператор который принудительно завершает работу цикла
# сontinue(продолжить) - оператор который пропускает итерацию если питон его встретит

# for i in range(1,11):
#     if i == 3:
#         continue
#     print(i)


# for i in range(1,11,2):
#     if i == 2:
#         continue
#     print(i)


# for i in range(1,11):
#     print(i)
#     if i == 3:
#         continue


# for i in range(1,11):
#     if i == 3:
#         break
#     print(i)


# for i in range(1,11):
#     print(i)
#     if i == 3:
#         break



# count = 0
# while count < 10:
#     print(count)
#     if count == 3:
#         continue
#     count += 1     


# count = 0
# while count < 10:
#     print(count)
#     if count == 3:
#         break
#     count += 1


# for i in range(1,11):
#     print(i)
#     if i == 3:
#         break
# else:
#     print('конец')


# else сработает тогда когда for завершит свою работу естественным путем, если цикл for завершается из за оператора break то else не сработает


# count = 0
# while count < 5:
#     print(count)
#     count += 1 
#     if count == 2:
#         break
# else:
#     print('цикл while завершил свою работу естественным путем')


# list2 = [23,'hi', True, None, 34, -23]
# count = 0
# while count < len(list2):
#     print(list2[count])                 # надо инкримент удалить и рассмотреть
#     count += 1



# list1 = [23,'hi', True, None, 34, -23]
# for i in list1:
#     a = list1.pop()
#     print(a)                                    # это тоже нужно рассмотреть


# list2 = [23,'hi', True, None, 34, -23]
# count = 0
# while count < len(list2):
#     print(list2.pop(count))                
#     count += 1
