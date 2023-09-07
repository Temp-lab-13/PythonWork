list_1 = "a a a b c a a d c d d"
list_2 = list_1.split()
dict ={}

for i in list_2:
    if i in dict:
        print(f'{i}_{dict[i]}', end=' ')
    else:
        print(i, end=' ')
    #dict[i] = dict.get(i,0) + 1
    dict[i] = dict.setdefault(i, 0) + 1
