# КАЛЬКУЛЯТОР 1.0
def pif():
    def o(a, b):
        c = a ** 2 + b ** 2
        d = c ** 0.5
        print("Результат вычисления длины гипотенузы: " + str(d))

    n = float(input())
    m = float(input())
    f = o(n, m)


def sr():
    def s(a, b):
        c = a ** (1 / b)
        print("Результат выделения корня из числа: " + str(c))

    k = float(input())
    g = float(input())
    l = s(k, g)


def unm():
    b = float(input())
    if b <= -1:
        c = b - b - b
        print(c)
    elif b >= 1:
        c = b - b - b
        print(c)
    elif b == 0:
        c = 0
        print("Результат вычисления унарного минуса: " + str(c))


def mod():
    j = float(input())
    if j <= -1:
        z = j - j - j
        print(z)
    elif j >= 1:
        z = j
        print(z)
    elif j == 0:
        z = 0
        print("Результат вычисления модуля числа: " + str(z))


def P():
    a2 = float(input())
    b2 = float(input())
    c2 = float(input())
    d2 = float(input())
    p1 = a2 + b2 + c2 + d2
    print("Результат вычисления периметра фигуры с 4-мя сторонами: " + str(p1))


def S():
    e = float(input())
    e1 = float(input())
    s1 = e * e1
    print("Результат вычисления площади прямоугольника: " + str(s1))


def V():
    a1 = float(input())
    b1 = float(input())
    c1 = float(input())
    v1 = a1 * b1 * c1
    print("Результат вычисления объёма паралелепипеда: " + str(v1))


def density():
    a3 = float(input())
    b3 = float(input())
    c3 = a3 / b3
    print('Результат вычисления плотности вещества' + str(c3))


def weight():
    a4 = float(input())
    v4 = float(input())
    w4 = a4 * v4
    print(str('Результат вычисления массы вещества' + str(w4)))


def circum():
    w = float(input())
    q = w * 3.14159256
    print('Результат вычисления длины окружности: ' + str(q))


def arci():
    r5 = float(input())
    a5 = 3.14159256 * 15 ** 2
    print('Результат вычисления площади окружности: ' + str(a5))


def volsp():
    r6 = float(input())
    v6 = (4 / 3) * 3.14159256 * r6 ** 3
    print('Результат вычисления объёма шара: ' + str(v6))


def fac():
    n = int(input())
    f = 1
    for i in range(1, n + 1):
        f = f * i
    print('Результат вычисления факториала числа: ' + str(f))


what = input("Выберите мат. действие: ")
if what == "+":
    a = float(input())
    b = float(input())
    c = a + b
    print('Результат вычисления суммы двух чисел: ' + str(c))
elif what == "-":
    a = float(input())
    b = float(input())
    c = a - b
    print('Результат вычисления разности двух чисел: ' + str(c))
elif what == "*":
    a = float(input())
    b = float(input())
    c = a * b
    print('Результат вычисления произведения двух чисел: ' + str(c))
elif what == "/":
    a = float(input())
    b = float(input())
    c = a / b
    print('Результат деления одного числа на другое: ' + str(c))
elif what == "**":
    a = float(input())
    b = float(input())
    c = a ** b
    print('Результат возведения в степень числа: ' + str(c))
elif what == "%":
    a = float(input())
    b = float(input())
    c = a % b
    print('Результат деления по модулю одного числа на другое' + str(c))
elif what == "-%-":
    a = float(input())
    b = float(input())
    c = a / 100 * b
    print('Результат вычисления процента от числа' + str(c))
elif what == "//":
    pif()
elif what == "/*":
    sr()
elif what == "--":
    unm()
elif what == "|":
    mod()
elif what == "P":
    P()
elif what == "S":
    S()
elif what == "V":
    V()
elif what == "p":
    density()
elif what == "m":
    weight()
elif what == "-0":
    circum()
elif what == "S0":
    arci()
elif what == "V0":
    volsp()
elif what == "!":
    fac()
else:
    print("Выбрана не предусмотренная операция!")
