
def f(a, b):
    resalt = a ** b
    return resalt

def f2(a, b):
    if b == 1:
        return a
    return a * f2(a, b - 1)

print(f(3, 4))
print(f2(3, 4))

