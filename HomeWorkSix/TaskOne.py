'''
Задача 30: 
Заполните массив элементами арифметической прогрессии. 
Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.

Пример:
Ввод: 7 2 5
Вывод: 7 9 11 13 15
'''
# Функция создаёт список с входными даннми от пользователя.
# Ввод каждого значения происходит с новой строки.
# Можно было и через цикл, но без поянений: что вводить?
# Я хотел с пояснениями.
def imputNumber():
    list_num = []
    list_num.append(int(input('Введите стартовое число: ')))
    list_num.append(int(input('Введите шаг прогрессии: ')))
    list_num.append(int(input('Введите количество элементов прогрессии: ')))
    return list_num

# Функция принимает результат другой функции, которым является список,
# с данными для формирования прогрессии.
# И возращает уже готовую прогрессию.
def progress(func):
    list_resalt = []
    # начинаем добавлять элементы со стартового значения func[0],
    # до последнего элемента плученного по формуле (с учотом того,
    # что в range не включается само указанное предельное значение),
    # и с шагом func[1]
    for i in range(func[0], func[0] + (func[2] * func[1]), func[1]):
        list_resalt.append(i)
    return list_resalt
    
# Запускаем функции и выводим результат их работы.
print(progress(imputNumber()))