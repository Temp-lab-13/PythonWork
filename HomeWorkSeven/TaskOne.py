''' 
Задача 34:  
Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

Пример:

Ввод: пара-ра-рам рам-пам-папам па-ра-па-да    
Вывод: Парам пам-пам  
'''
# Стих, для удобства проверки
verse = 'пара-ра-рам рам-пам-папам па-ра-па-да'
print(verse)

# Можно ввести в ручную.
# verse = input('Введите ситх: ')
# print(verse)

# Преобразуем в лист, разбивая фрвзу на части,
# Пробел используется как разделитель.
verse = verse.split(' ')
print(verse)


# Функция проверки. Принимает получившийся список.
def truVerse(verse): 
    f = []
    # Пробегаемся по списку и выписываем согласные в отдельный
    # список списков, где каждая фраза - отдельный список гласных. 
    for i in verse: 
        f.append(list(filter(lambda x: x in 'уеыаяиоэюё' or x == 'eayuio', i)))
    # Пробегаемся по новому списку проверяя равнозначность каждого подсписка.
    for x in range(len(f) - 1):
        # Стих считаеся правильным, если
        # колличество(!) гласных в каждой фразе одинаково,
        # при этом гласные могут отличаться, к примеру: а, е 
        if((lambda x: len(f[x - 1]) != len(f[x]))(x)):
           # Если условие сработола, значит проверка провалена.
           # Выводим грусную фразу и завершаем работу процедуры.   
           print('Пам парам')
           return
    # Если условие не сработало, то проверка пройдена, 
    # и мы выводм весёлую фразу.
    print('Парам пам-пам')

# Вызываем функцию проверки стиха
truVerse(verse)
    


