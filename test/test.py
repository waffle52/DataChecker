#!/usr/bin/env python3
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class MainApp(App):
    def build(self):
        layout = BoxLayout(padding=10)
        btn = Button(text="Button")
        layout.add_widget(btn)
        return layout

if __name__ == '__main__':
    app = MainApp()
    app.run()
