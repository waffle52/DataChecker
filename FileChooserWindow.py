#!/usr/bin/env python3
from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty

class MyWidget(GridLayout):
    def selected(self, filename):
        try:
            self.ids.image.source = filename[0]
        except:
            pass

class FileChooserWindow(App):
    def build(self):
        return MyWidget()

class SaveDialog(FloatLayout):
    save = ObjectProperty(None)
    text_input = ObjectProperty(None)
    cancel = ObjectProperty(None)

class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)
