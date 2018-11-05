from kivy.app import App
from random import random
from kivy.graphics import Line, Color
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from twilio.rest import Client
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.properties import ListProperty
from kivy.lang import Builder
from kivy.core.window import Window
Window.size = (750, 1334)


class Home(Screen):
    pass

class Bios(Screen):
    pass

class BiosTwo(Screen):
    pass

class BiosThree(Screen):
    pass

class jonathonBio(Screen):
    pass

class hanBio(Screen):
    pass

class luisBio(Screen):
    pass

class leoBio(Screen):
    pass

class vidaBio(Screen):
    pass

class cathyBio(Screen):
    pass

class annieBio(Screen):
    pass

class katBio(Screen):
    pass

class appaBio(Screen):
    pass

class steveBio(Screen):
    pass

class alyBio(Screen):
    pass

class mikaBio(Screen):
    pass

class davidBio(Screen):
    pass

class ianBio(Screen):
    pass

class loukaBio(Screen):
    pass

class wilburBio(Screen):
    pass

class picturesHome(Screen):
    pass

class picTwo(Screen):
    pass

class picThree(Screen):
    pass

class applyHere(Screen):
    pass

class applyTwo(Screen):
    pass

class applyThree(Screen):
    pass

class ScreenManagement(ScreenManager):
    pass

class touchInput(Widget):
    def on_touch_down(self, touch):
        print(touch)
    def on_touch_up(self, touch):
        print("released")
    def on_touch_move(self, touch):
        print("moving")

present = Builder.load_file("maine.kv")

class runApp(App):
    def build(self):
        return present

if __name__ == "__main__":
    runApp().run()
