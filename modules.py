from rich import print
from rich.console import Console

console = Console()

console.print("Hello", "World!", style="bold red")

# ФЕЙКОВЫЕ ДАННЫЕ
import random
from time import sleep
from tqdm import tqdm
from faker import Faker

fake = Faker('ru_RU')
for i in range(10):
    print(
        f"Name: {fake.name()}",
        f"Profession: {fake.job()}",
        f"Address: [i]{fake.address()}[/i]",
        f"Birthday: {fake.date_of_birth()}",
        f"Hair color: {fake.color_name()}",
        sep="\n"
    )

print(f"Взлом {fake.name()} аккаунта: ")
for i in tqdm(range(100), colour="green"):
    sleep(random.uniform(0.01, 0.1))
print(f"{fake.name()} ЛОХ ОБЬЕЛСЯ ЛОХ")

# ПАРСИНГ
"""from requests_html import HTMLSession

session = HTMLSession()
r = session.get("https://python.org")

pyver = r.html.find(".small-widget.download-widget a'",first=True)
print(pyver.text)"""

# ЧЕРЕПАХА
import turtle
import colorsys

t = turtle.Turtle()
turtle.Screen().bgcolor("black")
t.speed(100)
n = 36
h = 0
for i in range(460):
    c = colorsys.hsv_to_rgb(h,1,0.9)
    h += 1 / n
    t.color(c)
    t.left(145)
    for i in range(5):
        t.forward(300)
        t.left(150)

turtle.done()

# ЧЕРЕПАХА 2
import turtle

colors = ['red', 'blue', 'yellow', 'purple', 'pink', 'green']
t = turtle.Pen()
turtle.bgcolor('black')
for x in range(360):
    t.pencolor(colors[x % 6])
    t.width(x // 100 + 1)
    t.forward(x)
    t.left(59)
turtle.done()

# ГЕНЕРАТОР РАНДОМНЫХ ПАРОЛЕЙ
import random

lower = 'abcdefghjklmnopqrstuvwxyz'
upper = lower.upper()
sym = '!@#$%^&*-+=()|/>.;?№{}[]<>,:'
num = '1234567890'
together = lower + upper + sym + num
length = 10
password = ""
for _ in range(length):
    password = ''.join([password,random.choice(together)])

print(password)
