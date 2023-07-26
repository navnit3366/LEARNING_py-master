# 6 ЗАДАНИЕ
text = (input())
ind = text.find("f")
if True:
    print(ind)

# 5 ЗАДАНИЕ
numbers = [1.3, 65, 3543534, 2311, 33457]
for x in numbers:
    print(str(x) + " DIMA LOX")

for test in range(10):
    print("Hello")

# 7 ЗАДАНИЕ
import random

week_days = {
    0: 'воскресенье',
    1: 'понедельник',
    2: 'вторник',
    3: 'среда',
    4: 'четверг',
    5: 'пятница',
    6: 'суббота'
}
K = random.randrange(1, 366)
i = (1 + 3) % 7
print("1-е января: ", 1)
print("Номер дня недели: ", i)
print("День недели:", week_days[i])

# 8 ЗАДАНИЕ
a = int(input("Введите число: "))
if a in range(99, 1000):
    h = a // 100
    w = (a // 10) % 10
    d = a % 10
    if h < w < d:
        print("Да")
    else:
        print("Нет")

# 9 ЗАДАНИЕ
day_one = int(input("Введите км в 1 день: "))
y = int(input("Сколько должен пробежать: "))
a = 1
while day_one < y:
    day_one = day_one * 1.1
    a += 1
print(a)

# 10 ЗАДАНИЕ
a = int(input("Введите число: "))
b = 1
counter = 0
while b != 0:
    b = int(input("Введите число: "))
    if b >= a:
        counter += 1
    a = b
print(counter)

# 11 ЗАДАНИЕ
c = -1
d = 0
max_bebrovich = 0
numbers = int(input())
while numbers != 0:
    if c == numbers:
        d += 1
    else:
        c = numbers
        max_bebrovich = max(max_bebrovich,d)
        d = 1
    numbers = int(input())
max_bebrovich = max(d,max_bebrovich)
print(max_bebrovich)

# ЗАДАНИЕ 12
n1 = int(input())
dict1 = {}
for i in range(n1):
    lst = [str(s) for s in input().split(" ")]
    dict1[lst[0]] = list(lst[1:])
n2 = int(input())
for i in range(n2):
    lst1 = [str(s) for s in input().split(" ")]
    testlst = dict1[lst1[1]]
    if testlst.count("R") != 0:
        testlst.remove("R")
        testlst.append("read")
    if testlst.count("W") != 0:
        testlst.remove("W")
        testlst.append("write")
    if testlst.count("X") != 0:
        testlst.remove("X")
        testlst.append("execute")
    if testlst.count(lst1[0]) != 0:
        print("OK")
    else:
        print("Denied")
