
x = float(input("Nhap so x bat ki: "))
eps = pow(10, -6)
first = x
second = 2*(first + pow(x, 3)/3)
n = 2


def exp(n):
    a = 1
    b = n*2-1
    return a / b



while abs(first - second) > eps:
    n += 1
    first = second
    second = 2*(first/2 + exp(n)*pow(x, n*2-1))

print(first)
