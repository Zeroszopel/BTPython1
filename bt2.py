import math

x = float(input("Nhap so x bat ki: "))
eps = pow(10, -6)
first = float(1)
second = first - (2*3/2)*x
n = 1


def exp(n):
    a = (n+1)*(n+2)
    b = 2
    return a / b



while abs(first - second) > eps:
    n += 1
    first = second
    second = first + pow(-1, n)*exp(n)*pow(x, n)

print(first)


