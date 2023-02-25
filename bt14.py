def mul(y):
    s = 1
    for i in range(1, y + 1, 1):
        s *= i
    return s


x = float(input("Nhap so x bat ki: "))
eps = pow(10, -6)
first = 1
second = first + pow(x, 2)/mul(2)
n = 1


def exp(n):
    a = 1
    b = mul(n*2)
    return a / b



while abs(first - second) > eps:
    n += 1
    first = second
    second = first + exp(n)*pow(x, n*2)

print(first)
