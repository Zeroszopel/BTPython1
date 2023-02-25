def mul(y):
    s = 1
    for i in range(1, y + 1, 1):
        s *= i
    return s


x = float(input("Nhap giá trị x bất kì: "))
eps = pow(10, -6)
first = x
second = first + pow(x, 3) / mul(3)
n = 2


def exp(n):
    a = 1
    b = mul(n * 2 - 1)
    return a / b


while abs(first - second) > eps:
    n += 1
    first = second
    second = first + exp(n) * pow(x, n * 2 - 1)

print("Kết quả phép toán với x = ", x, " là: ", first)
