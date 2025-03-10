'============== JSON ================='
#JavaScript Object Notation - универсальный формат, в котором мы можем хранить данные в типах данных, понятных для всех языков программирования

import json 

json_list = "[null, true, 12, 4, 5]"

python_list = [None, True, 12, 4, 5]

# десериализация - перевод с json строки в python объект 
# loads - метод для десериализации с json строки
# load - метод для десериализации с json файла

python_data = json.loads(json_list)
# print(python_data) 

# with open('db.json') as file:
#     python_data1 = json.load(file)
    # print(python_data1)

# сериализация - перевод с python объекта в json строку
# dumps - метод для сериализации в json строку
# dump - метод для сериализации в json файл 

python_data2 = None
# json_data2 = json.dumps(python_data2)
# print(json_data2)

with open('db.json', 'w') as file:
    json.dump(python_data2, file) 
    


