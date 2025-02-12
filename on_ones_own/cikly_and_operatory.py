'================  Циклы и операторы в них  ================'


# цикл for 

# for i in range(1, 6, 2):
#     print(i)

# word = "hello world"
# for i in word:
#     print(i)

count = 0
word = "hello world"
for i in word:
    if i == 'o':
        count += 1 
print('caunt:', count)

'------- Цикл while ---------'
# i = 5 
# while i < 15:
#     print(i)
#     i += 2


# isHasCar = True

# while isHasCar:
#     if input('Enter data: ') == 'stop':
#         isHasCar = False

'---------- Операторы ------------'
# оператор 'break' - остановка 

# for i in range(1,11):
#     if i == 5:
#         break
    
#     print(i)

# # оператор 'continue' - пропускает итерацию в цикле

# for i in range(1,11):
#     if i % 2 == 0:
#         continue
#     print(i)

'----------- Корректный цикл ----------'

# found = None
# for i in 'hello':
#     if i == 'l':
#         found = True
#         break
# else:
#     found = False
# print(found)