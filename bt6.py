def mul(y):
    s = 1
    for i in range(1, y + 1, 1):
        s *= i
    return s


x = float(input("Nhap so x bat ki: "))
eps = pow(10, -6)
first = x
second = first - pow(x, 3)/mul(3)
n = 1


def exp(n):
    a = 1
    b = mul(n*2+1)
    return a / b



while abs(first - second) > eps:
    n += 1
    first = second
    second = first + pow(-1, n)*exp(n)*pow(x, n*2+1)

print(first)
