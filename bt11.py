x = float(input("Nhập giá trị x bất kì với x ∈ (-1, +1]: "))
while x <= -1 or x > 1:
    x = float(input("Nhập giá trị x bất kì với x ∈ (-1, +1]: "))

eps = pow(10, -6)
first = x
second = first - pow(x, 2) / 2
n = 2


def exp(n):
    a = 1
    b = n
    return a / b


while abs(first - second) > eps:
    n += 1
    first = second
    second = first - pow(-1, n) * exp(n) * pow(x, n)

print("Kết quả phép toán với x = ", x, " là: ", first)
