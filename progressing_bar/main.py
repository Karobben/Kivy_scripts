#!/usr/bin/env python3

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector

from kivy.clock import Clock
from kivy.lang import Builder

import time

class Paddle(Widget):
    Num = round(time.time() % 60 )
    score = NumericProperty(Num)

# First Module
class Single_bar(Widget):
    score = NumericProperty(0)
class Single_bar_B(Widget):
    score = NumericProperty(0)




class Main_app(Widget):
    bar_1 = ObjectProperty(None)



    def update(self, dt):
        self.bar_1.score = round(time.time() % 5 )
        self.bar_1.size = (40*(time.time() % 5), 20 )




class WeatherApp(App):
    def build(self):
        Main = Main_app()
        # Initialize
        Clock.schedule_interval(Main.update, 1/60)
        return Main

if __name__ == '__main__':
    WeatherApp().run()
