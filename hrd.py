class Jenya1:

    def dima(x, y):
        sum1 = x + y
        return sum1
    print(dima(1251255))

def oleg(x, y):
    if x < y:
        return x, True
    else:
        return y, False

print(oleg(34, 255))

def zhenya(l=None):
    if l is None:
        l = input().split()
    for x in range(len(l) - 1):
        if not l[x].isdigit() and not l[x+1].isdigit():
            print(l[x],l[x+1])
        if l[x].isdigit() and l[x + 1].isdigit():
            print(l[x], l[x + 1])

z = int(input())
result = []
while z > 0:
    result.append(z % 10)
    z //= 10
if sum(result[0:3]) == sum(result[3:6]):
    print("Ваш счаcтливый номер: ",result)


class City:

    def __init__(self, naselenie=1000000, square=1000, name="Tula"):
        self.naselenie = naselenie
        self.square = square
        self.name = name

    def nasvay(self):
        print(f"Население {self.name:} {self.naselenie}")


example = City()
example.nasvay()
example2 = City(15000000, 10000, "Elektrosral")
example2.nasvay()


class Elevator:

    def __init__(self, etazhi=5, current_et=3):
        self.etazhi = etazhi
        self.current_et = current_et

    def up(self):
        if self.current_et < self.etazhi:
            self.current_et += 1
            print("Вы поднялись на:", self.current_et, "этаж")

        else:
            print("Вы на максимальном этаже")

    def down(self):
        if self.current_et > 1:
            self.current_et -= 1
            print("Вы опустились на:", self.current_et, "этаж")

        else:
            print("Вы на первом этаже")


example3 = Elevator(10, 9)
example3.up()
example3.up()
example3.down()
example3.down()


class Elevator:
    def __init__(self, mx, now):
        self.mx = mx
        self.now = now
        print(f"Вы на {now}, максимум {mx} этажей")

    def up(self):
        if self.now < self.mx:
            self.now += 1
            print(f"Вы поднялись на {self.now} этаж")
            return True
        else:
            print(f"Вы сломали лифт")
            return False

    def down(self):
        if self.now > 1:
            self.now -= 1
            print(f"Вы опустились на {self.now} этаж")
            return True
        else:
            print(f"Вы сломали лифт")
            return False

def process(e,i):
    while i:
        y = input("1 - подняться, 2 - опуститься \n")
        if y == "1":
            i = e.up()
        elif y == "2":
            i = e.down()
        else:
            print("Error")

i = True
mXF = int(input("Максимальный этаж: "))
CF = int(input("На каком вы этаже: "))
a = Elevator(mXF,CF)
process(a,i)

from math import log


def __init__(a,what: str or float,b):
    # Я НИХУЯ НЕ ПОНИМАЮ БЛЯТЬ!!! 3:26 14.11.22
    if what == "+":
        print(f'Результат вычисления суммы двух чисел: {a + b}')
        return a + b
    elif what == "-":
        print(f'Результат вычисления разности двух чисел: {a - b}')
        return a - b
    elif what == "*":
        print(f'Результат вычисления произведения двух чисел: {a * b}')
        return a * b
    elif what == "/":
        print(f'Результат деления одного числа на другое: {a / b}')
        return a / b
    elif what == "**":
        print(f'Результат возведения в степень числа: {a ** b}')
        return a ** b
    elif what == "ln":
        print(f'Результат вычисления натурального логорифма: {log (a)}')
        return log(a)

x = None
i = 1
while x != "0":
    if i == 1:
        x = str(input("Выберите мат. действие: "))
        a = float(input("Введите 1 число: "))
        b = float(input("Введите 2 число: "))
        a = __init__(a,x,b)
        i += 1
    else:
        x = str(input("Выберите мат. действие: "))
        b = float(input("Введите 2 число: "))
        a = __init__(a,x,b)

    c = input("Продолжить - 1\nЗакончить - 2\n")
    if c == "1":
        continue
    else:
        break
