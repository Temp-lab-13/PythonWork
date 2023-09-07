def sum(a, b):
    if a != 0: 
        return sum(a - 1, b + 1)
    return b

    
print(sum(30, 5))


