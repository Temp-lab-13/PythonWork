

def get_work(n):
    n1 = int((n / 3) / 2)
    n3 = int(n1)
    n2 = int((n1 + n3) * 2)
 
    return n1, n2, n3
n = 60

n1, n2, n3 = get_work(n)
print(n1, n2, n3)
