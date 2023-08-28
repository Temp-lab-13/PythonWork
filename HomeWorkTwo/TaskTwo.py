# Импортируемый модуль, что бы работала рандомная генерация чисел.
import random
'''
Петя и Катя – брат и сестра. Петя – студент, а Катя –
школьница. Петя помогает Кате по математике. Он задумывает два
натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
этого Петя делает две подсказки. Он называет сумму этих чисел S и их
произведение P. Помогите Кате отгадать задуманные Петей числа.
'''
# Получаем рандомно два числа загаданных Петей.
X = random.randint(1, 1001)
Y = random.randint(1, 1001)
# Выводим, что потом сверить с ними ответ.
print(f"Число Х: {X}; Число Y: {Y}.")
# Получаем подсказки. 
# Сумма и произведение загаданных чисел.
summa = X + Y
product = X * Y
# Пременные в которые сохраним наш ответ.
y = 0
x = 0
# С помощью цикла перебираем числа. i - потенциальный y, а разность между суммой чисел(подсказка Пети) и проверяемого значения i, соответсвенно потециальный х.
for i in range(1, summa):
    temp = summa - i
    # Если проверяемые числа(i(y) и temp(x)),
    # равны произведению чисел из подсказки,
    # то мы нашли искомые числа.
    if product == (temp * i):
        y = i
        x = temp
print(f"Загаданные числа Х: {x}; а Y: {y}.")    


    