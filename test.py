#!/usr/bin/env python3
import kivy
import os
from FileChooserWindow import *
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle
from kivy.uix.image import Image
kivy.require('1.9.0')
from kivy.lang import Builder
from kivy.config import Config
from kivy.uix.textinput import TextInput
from kivy.app import App

#test
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_string('''
''')

class CustomLayout(FloatLayout):
    def __init__(self, **kwargs):
        # make sure we aren't overriding any important functionality
        super(CustomLayout, self).__init__(**kwargs)

        with self.canvas.before:
            Color(0.411, 0.411, 0.411, 0.411)
            self.rect = Rectangle(size=self.size, pos=self.pos)

        self.bind(size=self._update_rect, pos=self._update_rect)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

class MainApp(App):
    def callback(self, event):
        #window = FileChooserWindow()
        #window.run()
        pass

    def build(self):
        self.title = 'WestCal DataChecker'
        layout = CustomLayout()
        src = "{}/images/WestCal_Logo.png".format(os.getcwd())
        img = Image(source=src, size_hint_y=(.5), size_hint_x=(.25), pos_hint={'x':0.007, 'y':0.565})
        btn1 = Button(text='Select File', size_hint=(.2, .1), pos_hint={'x':0.3, 'y':0.35})
        btn2 = Button(text='Check File', size_hint=(.2, .1), pos_hint={'x': 0.5, 'y': 0.35})
        l = Label(text='Enter Max Search Length:', markup=True, size_hint=(1, 1), pos_hint={'x': -0.15, 'y': 0.08}, font_size='50')
        sec_l = Label(text='File Selected:', markup=True, size_hint=(.8, .8), pos_hint={'x': -0.12, 'y': 0.10}, font_size='40')
        third_l = Label(text='Test.xlsx', markup=True, size_hint=(.8, .8), pos_hint={'x': 0, 'y': 0.098})
        textinput = TextInput(text='', multiline=False, size_hint=(.3, .08), pos_hint={'x': 0.538, 'y': 0.54})
        btn1.bind(on_press = self.callback)

        layout.add_widget(img)
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(l)
        layout.add_widget(sec_l)
        layout.add_widget(third_l)
        layout.add_widget(textinput)
        return layout

if __name__ == '__main__':
    app = MainApp()
    Config.set('graphics', 'resizable', False)
    app.run()
