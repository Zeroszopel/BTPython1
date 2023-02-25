
x = float(input("Nhap so x bat ki: "))
eps = pow(10, -6)
first = x
second = first - pow(x, 2)/2
n = 2


def exp(n):
    a = 1
    b = n
    return a / b



while abs(first - second) > eps:
    n += 1
    first = second
    second = first - pow(-1, n)*exp(n)*pow(x, n)

print(first)
