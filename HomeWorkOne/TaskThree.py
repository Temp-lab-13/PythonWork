def calc_luck(n, length):
    res = 0
    for x in n[:length]:
        res += int(x)
    res2 = 0
    for x in n[length:]:
        res2 += int(x)
    
    return res == res2


n = 385916
n = str(n)
lenght = int(len(n) / 2)
resalt = calc_luck(n, lenght)

if resalt:
    print('yes')
else:
    print('no')
