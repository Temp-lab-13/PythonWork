'''
Задача № 22
Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.

Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

Пример:
Превый ряд: 11 6 2 4 6 8 10 12 10 8 6 4 2
Второй ряд: 3 6 9 12 15 18
Результат: 6 12
'''
# Импортируем фенкционал рандома.
import random

# Функция заолняющая список по его длине рандомными числами.
def randomImput (length):
    return [random.randint(0, 50) for i in range(length)]
# Сортировка. Интерса ради.
def q_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    return (q_sort(less) + [pivot] + q_sort(greater)) 

# Вводим длину каждого списка, как в условии. 
lengthList_1 = int(input('Введите колличество элементов первого ряда: '))
lengthList_2 = int(input('Введите колличество элементов второго ряда: '))

#Создаём списки указанного размера.
# Но что бы не заполнять в ручную, используем генератор списков.
List_1 = randomImput(lengthList_1)
List_2 = randomImput(lengthList_2)
# Проверка, что списки заполнены корректно.
print(f"Первый ряд чисел: {List_1}")
print(f"Второй ряд чисел: {List_2}")
# Конвертируем списки в множества и сразу же
# Объединяем пересекающиеся элементы в отдельную переменную.
resalt = set(List_1).intersection(set(List_2))
# Вывод отсортированного множества.
print(f"Вариант 1: {sorted(resalt)}")
# Выод отсортированого листа.
print(f"Вариант 2: {q_sort(list(resalt))}")


