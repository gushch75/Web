
n=int(input ('Введите натуральное число N : '))
def Factor(n):
    array = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            array.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        array.append(n)
    return array
print (Factor(n))
