import os
from turtledemo.chaos import g

import b
import hw

time = input("set your time!")
if time == " Day" or "day":
    print("Go for a walk!")
elif time == " Night " or "night":
    print("Go to sleep!")
else:
    print("Are you dumb" + "?")

# ЦИКЛЫ
i = 1000
while i <= 100:
    print(i)
    i = i + 5
i = False

# ОБХОД ЦИКЛОВ
numbers = [1.3, 65, 3543534, 2311, 33457]
for x in numbers:
    print(str(x) + "@")

for test in range(100):
    print("Hello")

# БЕСКОНЕЧНЫЙ ЦИКЛ
i: int = 1000
while 1 == 1:
    print(str(i) + " OLEG ")
    i = 1000 * 1 + i ** 2
    if i == 1032501012649311092586025722236772170064401929913377683866584730972024704168191423653197506528877466369654150869425053464559365451614714485399916125717722295918398950365132042014005002001001000:
        break
print("You are dolboeb")

# ЗАДАЧИ
number = 0
while number <= 1000:
    number += 1
    if (number % 2) != 0:
        continue
    print("current data " + str(number))

# СПИСКИ
index: list[int] = [1, 2, 3, 4, 5]
print(index[2])

index: list[int] = [1, 6, [1, 3]]
print(index + [1, 2, 3])

index: list[str] = ["Oleg", "Ivan", "Pidr"]
if "Oleg" in index:
    print(2)
if "Luda" in index:
    print(1)
else:
    print(0)

index: list[str] = ["Today we have a list of top 5 racoons!"]
print(index[0])

test = []
test.append("Hello World! " + str(123))
print(test)

test = [2, 3, 4, 8, 11, 0, 5, 7]
test.append(5)
print("We have a list of top " + str(len(test)) + " racoons")
test.remove(5)
print("We have a list of top " + str(len(test)) + " racoons")

test = [1.3, 1.77, 34.443]
test.insert(0, 4)
print(test)

test = [0, 233233, 323231542, 42356476574323, 35245246, 4564764352, 36345436346, 233233, 233233, 233233]
test.reverse()
print(test)
print(max(test))
print(min(test))
print(test.count(233233))

# ДИАПАЗОНЫ
number = list(range(int(1.5), 101, 2))
print(number)


# СВОИ ФУНКЦИИ
def multiply(number1):
    print(number1 ** 10)


multiply(2)


def max(x, y):
    if x > y:
        return x
    elif x < y:
        return y


x = float(input("Number 1:"))
y = float(input("Number 2:"))
print(max(2323, 4324))


def spam_point():
    print("You're idiot")


spam_point()
spam_point()
spam_point()
while 1 == 1:
    print("Not spamming")
    if spam_point() == "You're idiot/nNot spamming":
        break


def hello():
    """ОПИСАНИЕ ФУНКЦИИ(ЧТО ОНА ДЕЛАЕТ)"""
    print("HEllo!")


my_idea = hello
my_idea()


def hi(name1):
    print("fuck you!" + name1)


def hello():
    return " $$$" + input("Your name:") + "$$$ "


hi(hello())


def hi(name2):
    print("fuck you!" + name2())


def hello():
    return " $$$" + input("Your name:") + "$$$ "


hi(hello)

# МОДУЛИ И ИХ ИМПОРТ
import random

for i in range(10):
    print(random.randint(10, 1000))

from math import *

print(sqrt(1024))
print(pi)

from math import sqrt as biskovna_est_pechenie

print(biskovna_est_pechenie(144))

# ИСКЛЮЧЕНИЯ И СВОИ ИСКЛЮЧЕНИЯ
try:
    a = 3
    print(7 / 0 + 3)
    print(b)
    eval("print(7/0)abc")
except ZeroDivisionError:
    print("HOLY SHIITE")
except NameError:
    print("SHIITE")
except(IndexError, TypeError, IndentationError):
    print("Unknown Command")
except TypeError:
    print("Your Error")
finally:
    print("The end")

print("Program Finished!")

try:
    a = "Good job!"
    if a == "Good job!":
        raise TypeError
except TypeError:
    print("Bad job!")

# pof = "bad hw"
# if pof == "bad hw":
# raise TypeError("You lose")

# class BishkovnaError(Exception):
# pass

# raise BishkovnaError("Test")

# def test(number):
# assert number >= 0, "Number should be more than 0"
# print(str(number))
# test(10)
# test(-10)

# РАБОТА С ФАЙЛАМИ
filename = input("Select File Name:")
if FileNotFoundError:
    print("Choose another file!")
file = open(filename, "r")
print("In this file " + str(len(file.read())) + " symbols")

file.close()

filename = input("Choose File Name: ")
text = input("Your text:")
file = open(filename, "w")
file.write(text)

file.close()

filename = input()
file = open(filename, "a")
file.write(" HFJHFDSHFFFSHDKFF")

file.close()

# r - Чтение файла
# w - Перезапись файла
# a - Добавление в файл
# b - Binary mode

# СОЗДАНИЕ БЭКАПОВ
filename1 = input("Which backup file do you want?: ")
filename2 = "backup_" + filename1
file1 = open(filename1, "rb")
file2 = open(filename2, "wb")
file2.write(file1.read())

file1.close()
file2.close()

with open("../../Documents/Python Scripts/text.txt", "r") as f:
    print(f.read(5))
    print(f.read())

# СЛОВАРЬ
test = dict(key1="num2", key2="num 5", key3="num 0")
print(test["key1"])

try:
    print(test["key4"])
except KeyError:
    print("N0NE")

text = None
print(text)


def test():
    print("TEST")


text = ()
print(text)

trent = {
    "korn1": "2",
    "korn2": "3",
    "korn3": "4",
    300: "Three hundred bucks"
}
if 300 in trent:
    print("exist")
elif 300 not in trent:
    print("didn't exist")
else:
    print("absent")

testing = input("Contact: ")
if testing in trent:
    print("Contact:" + trent[testing])
else:
    print("Contact not found")

print(trent.get("korn1"))
print(trent["korn2"])

# СРЕЗ СПИСКА
digit = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
for x in digit:
    print(str(x) in range(0, 10))
digits2 = digit[2:5:3]
digits3 = digit[-5:-1]
digits4 = digit[::-1]
print(digits2)
print(digits3)
print(digits4)

# ФОРМАТИРОВАНИЕ СТРОК
name = "Bruce"
age = 21

print("Hello, %s!\nYou are already %d years old!" % (name, age))

# %s - Форматирование строки(string)
# %d - Форматирование числа
# %f - Форматирование дроби(float)

print("Hello, {}!\nYou are already {} years old!".format(name, age))
print("{0}\n{1}{1}".format("vanya", "gey "))
person = "Ibrahim"
personal = 22
print("Hello, {name}!\nYou are already {age} years old!".format(name=person, age=personal))

human = {
    "Age": 21,
    "Name": "Donald"
}
print("Your age: {age}\nYour name: {name}".format(name=human["Name"], age=human["Age"]))
print("Your age: {person[Age]}\nYour name: {person[Name]}".format(person=human))

a = "Oleg"
# Oleg**** - <
# ****Oleg - >
# **Oleg** - ^
length = 10

if len(a) % 2:
    length -= 1

print("Hello! {0:*^10}".format(a) + " Bro")
#                   ^это число символов(в данном случае звездочек)

inp = input('Your name: ')
print(('{0:*^' + str(10 + (len(inp) % 2)) + '}').format(inp))

# ФУНКЦИИ ДЛЯ РАБОТЫ СО СТРОКАМИ И ЧИСЛАМИ
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
fruits = "Banana, Apple, Grapefruit, Cherry, Kiwi"

# join, replace, startswith, endswith, lower, upper, split, min, max, abs, sum
print(min(numbers))
print(max(numbers))
print(sum(numbers))
print(' - '.join(fruits))
print("Hello World!".replace("World", "Galaxy"))
print(fruits.split(","))

name = input("Your name: ")
if name.lower().startswith("o") or name.lower().startswith("о"):
    print("Oh,You cool!")
else:
    print("You are GAY!")

name = input("Your name: ")
if name.upper().endswith("ING"):
    print("Hello ING!")
else:
    print("WTF?")


def toHex(red=None, green=None, blue=None):
    return "#%02x%02x%02x" % (red, green, blue)


class Color:
    red = 0
    green = 0
    blue = 0

    def __init__(self, r, g, b):
        self.red = r
        self.green = g
        self.blue = b


class Alpha:
    red = r
    green = g
    blue = b
    alpha = a

    def __init__(self, r, g, b, a):
        self.red = r
        self.green = g
        self.blue = b
        self.alpha = a


# серый цвет
gray = Color(80, 80, 80)
# наполовину прозрачный красный цвет
red = Alpha(255, 0, 0, .5)

# ИМПОРТ МОДУЛЕЙ
import sys

if __name__ == "__main__":
    print(dir(hw))
    print(sys.path)

# МНОЖЕСТВА
# список
x = [1, 2, 3, 4, 5, 6, 7, 8]
# словарь
z = dict(key1="lol", key2="lox", key3=x)
# кортеж
v = (0, -1, -2, -3, -4, -5, -6, -7, -8)
# множества
s = {1, 2, 3, 4, 5, 6, 7, 8}
print(x.__sizeof__())
print(z.__sizeof__())
print(v.__sizeof__())
print(s.__sizeof__())

# НОВЫЕ МЕТОДЫ
s.update(v)
s.discard(6)
e = s.intersection(v)
t = s.difference(v)
print(s, e, t)
# функция отвечает за путь к файлу
os.walk("C:")


# ФУНКЦИЯ ARGS
def f(*args, key=False):
    list1 = []
    for i2 in args:
        for y2 in i2:
            if y2 not in list1:
                list1.append(y2)
    if key:
        list1.sort()
    return list1


num1 = [23, 51, 14]
num2 = [24, 15, 61]
num3 = [2, 46, 1, 8]

t1 = f(num1, num2, num3, key=True)
print(t1)

# РАБОТА С МОДУЛЕМ TIME
import time

a = list(range(10000))
b = list(range(5000, 10000))
c = list(range(1000, 2000))

start = time.time()
f = (a, b, c)
stop = time.time() - start
print(stop)

start2 = time.time()

d = set(a)
# .union обьединяет значение двух списков
e = d.union(set(b), set(c))
stop2 = time.time() - start
print(start2)

new = set()
fr = open("../../Documents/Python Scripts/debug.log")
new.update(set(fr.read().split()))
fr.close()
print(new)

# ГЕНЕРАТОРЫ
k = [91, 38, 41, 55, 21, 4, 551, 84]
new1 = []
for x in k:
    new1.append(x * 2)
print(new1)

new2 = [x * 2 for x in k]
print(new2)

new3 = {x * 2 for x in k}
print(new3)

new4 = {x: x * 2 for x in k}
print(new4)

new5 = [x for x in k if x % 2 == 0 and x > 0]
print(new5)


def some():
    list_test = []
    with open("../../Documents/Python Scripts/text.txt", encoding="utf-8") as r:
        for x6 in r:
            list_test.append(x6)
    return list_test


for i in some():
    print(i.split())


def another():
    with open("../../Documents/Python Scripts/text.txt", encoding="utf-8") as r:
        for x2 in r:
            yield x2


for i in some():
    print(i.split())

p = another()
print(next(p))
print(next(p))
print(next(p))
print(next(p))
for x in p:
    print(x)


# ФУНКЦИЯ LAMBDA
def vanya(x5):
    return x5 / 5


var = lambda x5: x5 / 5

print(vanya(555))
print(var(555))

list_of = [["Oleg", 17], ["Dima", 16], ["x", 333 / 3 * 10]]


def sap(x5):
    return x5[1]


s = sorted(list_of, key=sap)
print(s)

s = sorted(list_of, key=lambda x5: x[1])
print(s)

x1 = list(filter(lambda x5: x5[1] > 18, list_of))
print(x1)

# ООП
import acccessify
from accessify import private, protected


class Point:
    color = "red"
    circle = 2
    square = 4

    @private  # модуль accessify
    @classmethod  # Декортаор
    def value(cls, arg):
        return cls.square <= arg <= cls.circle

    def __new__(cls, *args, **kwargs):
        print(str(cls))
        return super().__new__(cls)

    def __init__(self, x, y):
        print(str(self))
        self.x = x
        self.y = y

    def set_chords(self, x, y):  # СЕТТЕРЫ
        if type(x) in (int, float) and type(y) in (int, float):
            self.x = x
            self.y = y

    def get_chords(self):  # ГЕТТЕРЫ
        return self.x and self.y

    @staticmethod  # Декоратор
    def quadrat_normi(x, y):
        return x * x + y * y


pt = Point(366, 367)
pt.set_chords(1, 2)
print(pt.__dict__)
print(Vector.quadrat_normi(5, 6))


class dataBase:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __del__(self):
        dataBase.__instance = None

    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port

    def connect(self):
        print(f'Connecting with dataBase: {self.user},{self.psw},{self.port}')

    @staticmethod
    def close():
        print('close connection with dataBase')

    @staticmethod
    def read():
        return 'data from dataBase'

    @staticmethod
    def write(data):
        print(f'rec in dataBase {data}')

    def __getattribute__(self, item):
        if item == 'db':
            raise ValueError('blocked')
        else:
            return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        if key == 'z':
            raise AttributeError('none')
        else:
            return object.__setattr__(self, key, value)

    def __getattr__(self, item):
        return False

    def __delattr__(self, item):
        object.__delattr__(self, item)


db = dataBase('root', 1234, 80)
db2 = dataBase('root', 5432, 40)
db.connect()
db2.connect()
print(id(db), id(db2))
del db.user

# public:
attribute = 10
# protected:
_attribute2 = 10
# private:
__attribute3 = 10


# МОНОСОСТОЯНИЕ
class ThreadData:
    __shared_attrs = {
        'name': 'thread_1',
        'data': {},
        'id': 1
    }

    def __init__(self):
        self.__dict__ = self.__shared_attrs


th1 = ThreadData()
th2 = ThreadData()
th2.id = 3

th1.attr = 'new_attr'


# PROPERTY
class Person:

    def __init__(self, age, name):
        self.__old = None
        self.__name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    age = property(get_age, set_age)
    age = age.getter(get_age)
    age = age.setter(set_age)

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, old):
        self.__old = old

    @old.deleter
    def old(self):
        del self.__old


p = Person('Oleg', 17)
p.__dict__['old'] = 'old in obj "p"'
a = p.age
p.age = 35
del p.old
print(p.age, p.__dict__)
print(p.old, p.__dict__)


class hueta:
    s_rus = 'qwertyuiopasdfghjklzxcvbnm'
    s_rus_upper = s_rus.upper()

    def __init__(self, fio, old, passport, weight):
        self.__fio = fio.split()
        self.__old = old
        self.__passport = passport
        self.__weight = weight

        self.verify(fio)
        self.verify_1(old)
        self.varify(weight)
        self.varify_1(passport)

    @classmethod
    def verify(cls, fio):
        if type(fio) != str:
            raise typeerror('must be a string')

        f = fio.split()
        if len(f) != 3:
            raise typeerror('idiot')

        letters = ascii_letters + cls.s_rus + cls.s_rus_upper
        for s in f:
            if len(s) < 1:
                raise typeerror('idiot')
            if len(s.strip(letters)) != 0:
                raise typeerror('idiot')

    @classmethod
    def verify_1(cls, old):
        if type(old) != int or old < 14 or old > 120:
            raise TypeError('must be in [from 14 to 120]')

    @classmethod
    def varify(cls, weight):
        if type(weight) != float or weight < 20:
            raise TypeError('')

    @classmethod
    def varify_1(cls, passport):
        if type(passport) != str:
            raise TypeError('must be a string')

        s = passport.split()
        if len(s) != 2 or len(s[0] != 4 or len(s[1])) != 6:
            raise TypeError('idiot')

        for p in s:
            if not p.isdigit():
                raise TypeError('idiot')

    @property
    def fio(self):
        return self.__fio

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, old):
        self.verify_1(old)
        self.__old = old

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.varify(weight)
        self.__weight = weight

    @property
    def passport(self):
        return self.__passport

    @passport.setter
    def passport(self, passport):
        self.varify_1(passport)
        self.__passport = passport


p = Hueta('Bashtanar Oleg Alexandrovich', 17, '1234 567890', 70.5)
p.old = 100
p.passport = '1234 876543'
p.weight = 70.0
print(p.old, p.passport, p.weight)


# ДЕСКРИПТОРЫ
class ReadIntX:
    def __set_name__(self, owner, name):
        self.name = '_x'

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    # def __set__(self, instance, value):
    # setattr(instance,self.name,value)


class Int:
    @classmethod
    def coord(cls, coord):
        if type(coord) != int:
            raise TypeError(' must be an integer')

    def __set_name__(self, owner, name):
        self.name = '-' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.coord(value)
        instance.__dict__[self.name] = value


class Point:
    x = Int()
    y = Int()
    z = Int()
    xr = ReadIntX()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


p = Point(1, 2, 3)
p.xr = 5
# p.__dict__['xr'] = 5
print(p.xr, p.__dict__, p.z)

#ПАРСИНГ
from bs4 import BeaitifulSoup

with open("C:\Users\bashka\Downloads\Telegram Desktop\23тест",encoding="utf-8") as file:
    src = file.read()
# print(src)

soup = BeautifulSoup(src,'lxml')
