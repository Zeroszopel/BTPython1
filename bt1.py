# This is a sample Python script.
import math

x = int(input("Nhập giá trị x bất kì "))
eps = pow(10, -6)
first = 1
second = first + (x / 1)
n = 1


def mul(y):
    s = 1
    for i in range(1, y + 1, 1):
        s *= i
    return s


def exp(x, n):
    a = pow(x, n)
    b = mul(n)
    return a / b


while abs(first - second) > eps:
    n += 1
    first = second
    second = first + exp(x, n)

print("Kết quả phép toán với x = ", x, " là: ", first)
