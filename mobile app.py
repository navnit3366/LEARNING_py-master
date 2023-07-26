import My as My
from kivy.app import App
from kivy.lang import Builder

kv = """
FloatLayout:
    Button:
        text: "Hello World!"
        size_hint: None, None
        pos_hint: {'center_x': 0.5},
        {'center_y': 0.5}
        canvas.before:
            PushMatrix
            Rotate:
                angle: 45
                origin: self.center
        canvas.after:
            PopMatrix
        """
class SuperApp(App):
    def build(self):
        return Builder.load_string(kv)

SuperApp.run()


# РАБОТА С KIVY, РАЗРАБОТКА МОБИЛЬНЫХ ПРИЛОЖЕНИЙ
from kivy.uix.codeinput import CodeInput
from pygments.lexers import HtmlLexer
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter

from kivy.config import Config
Config.set("graphics", "resizable", "0")
Config.set("graphics", "height", "1600")
Config.set("graphics", "width", "900")


def build():
    s1 = Scatter()
    fl = FloatLayout(size=(300,300))
    s1.add_widget(fl)
    fl.add_widget(Button(text="Hello World!", font_size=14, on_press=btn_press, background_color=[.85,.64,.21,1],
                  background_normal="", size_hint=(.5,.25),pos=(1600 / 2 - 400, 900 / 2 - (900 * .25 / 2))))
    return s1


def btn_press(i1):
    instance = i1
    print("Button already pressed")
    i1.text("I'm pressed")

    return CodeInput(Lexer=HtmlLexer())

class Appearance(My):
    pass

if __name__ == "__main__":
    Appearance().run()

# ВИДЖЕТЫ BOXLAYOUT,GRIDLAYOUT И ANCHORLAYOUT
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.textinput import TextInput

class Boxxx(App):

    def build(self):
        b1 = BoxLayout(orientation='horizontal',
                       padding=[50,25],
                       spacing=100)

        b1.add_widget(Button(text='Button 1'))
        b1.add_widget(Button(text='Button 2'))
        b1.add_widget(Button(text='Button 3'))

        return b1

    def builer(self):
        g1 = GridLayout(cols=3,
                        rows=10,
                        padding=[30],
                        spacing=3)

        for x in range(30):
            g1.add_widget(Button(text="XYZ"))

        return g1

    def builders(self):
        a1 = AnchorLayout()

        a1.add_widget(Button(text="Button",
                             size_hint=[.5,.5]))

        return a1

    def builder(self):
        t1 = BoxLayout(orientation='vertical',
                       size_hint=[.5,.5])
        t2 = AnchorLayout()

        t1.add_widget(TextInput())
        t1.add_widget(TextInput())
        t1.add_widget(Button(text="Enter"))

        t2.add.widget(t1)

        return t2

if __name__ == "__main__":
    Boxxx().run()

# КАЛЬКУЛЯТОР
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.config import Config
Config.set('graphics','resizable',0)
Config.set('graphics','width',400)
Config.set('graphics','height',500)

class Calculate(App):

    def update(self):
        self.lbl.text = self.formula

    def number(self, instance):
        if self.formula == "0":
            self.formula = ""

        self.formula += str(instance.text)
        self.update_label()

    def operation(self,instance):
        if str(instance.text).lower() == "x":
            self.formula += "*"
        else:
            self.formula += str(instance.text)
        self.update_label()

    def result(self):
        self.lbl.text = str(eval(self.lbl.text))
        self.formula = "0"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.lbl = None
        self.formula = None
        self.lb1 = None

    def build(self):
        self.formula = "0"

        b1 = BoxLayout(orientation='vertical', padding=25)
        g1 = GridLayout(cols=4,spacing=3,size_hint=(1,.6))

        self.lb1 = Label(text='0',font_size=40,halign="right",valign='center',
                         size_hint=(1,.4),text_size=(400 - 50,500 * .4 - 50))
        b1.add_widget(self.lb1)

        g1.add_widget(Button(text="7",on_press=self.number))
        g1.add_widget(Button(text="8",on_press=self.number))
        g1.add_widget(Button(text="9",on_press=self.number))
        g1.add_widget(Button(text="x",on_press=self.operation))

        g1.add_widget(Button(text="4",on_press=self.number))
        g1.add_widget(Button(text="5",on_press=self.number))
        g1.add_widget(Button(text="6",on_press=self.number))
        g1.add_widget(Button(text="-",on_press=self.operation))

        g1.add_widget(Button(text="1",on_press=self.number))
        g1.add_widget(Button(text="2",on_press=self.number))
        g1.add_widget(Button(text="3",on_press=self.number))
        g1.add_widget(Button(text="+",on_press=self.operation))

        g1.add_widget(Widget())
        g1.add_widget(Button(text="0",on_press=self.number))
        g1.add_widget(Button(text=".",on_press=self.number))
        g1.add_widget(Button(text="=",on_press=self.result))

        g1.add_widget()
        return b1

    def update_label(self):
        pass


if __name__ == "__main__":
    Calculate().run()

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import (Color, Line)

class Painter(Widget):
    def __init__(self,**kwargs):
        super(Painter,self).__init__(**kwargs)

        with self.canvas:
            Color(0,1,0,1)
            self.line = Line(points=(),width=10)

    def on_touch_down(self, touch):
        self.line.points += (touch.x,touch.y)

class Paint(App):
    def build(self):
        return Painter()

if __name__ == "__main__":
    Paint().run()
