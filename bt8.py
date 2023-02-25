def mul(y):
    s = 1
    for i in range(1, y + 1, 1):
        s *= i
    return s


x = float(input("Nhập giá trị x bất kì với x ∈ (-1, +1): "))
while x <= -1 or x >= 1:
    x = float(input("Nhập giá trị x bất kì với x ∈ (-1, +1): "))

eps = pow(10, -6)
first = x
second = first + (1 / 2) * pow(x, 3) / 3
n = 1


def exp(n):
    a = 1
    b = 1
    for i in range(1, n + 1, 1):
        a *= i * 2 - 1
    for j in range(1, n + 1, 1):
        b *= j * 2
    return a / b


while abs(first - second) > eps:
    n += 1
    first = second
    second = first + exp(n) * pow(x, n * 2 + 1) / (n * 2 + 1)

print("Kết quả phép toán với x = ", x, " là: ", first)
