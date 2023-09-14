'''
Требуется найти в массиве list_1 самый близкий по величине элемент к заданному числу k и вывести его. 

Пример:

list_1 = [1, 2, 3, 4, 5]
k = 6
Резултат: 5

'''

list_1 = [1, 12, 6, 7, 8, 15]
k = 11
element = 0
temp = 0
flag = True

for x in list_1:
    if x == k:
        element = x
    elif x < k:
        if x > element and x < k:
            element = x

for x in list_1:
    if x > k:
        temp = x

for x in list_1:
    if x > k and temp > x:
        temp = x

countOne = 0
countTwo = 0 
if temp != 0:
    while flag:
        if element != k:
            countOne += 1
            element += 1
        elif temp > k:
            countTwo += 1
            temp -=1
        else:
            flag = False
    if countOne > countTwo:
        print(temp + countTwo)
    else: print(element - countOne)
else: print(element)




