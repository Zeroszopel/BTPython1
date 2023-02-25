x = float(input("Nhap so x bat ki: "))
eps = pow(10, -6)
first = 1
second = first +(1/2)*x
n = 1


def exp(n):
    a = 1
    b = 1
    for j in range (1,n+1,2):
        a*=j
    for i in range (1,n+1,1):
        b*=i*2
    return a / b



while abs(first - second) > eps:
    n += 1
    first = second
    second = first - pow(-1,n)*exp(n)*pow(x,n)

print(first)
