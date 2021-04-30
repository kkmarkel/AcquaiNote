import os
import sys

from kivy.app import App

# from kivymd.app import MDApp
# from kivymd.theming import ThemeManager
# from kivymd.navigationdrawer import NavigationDrawer

# from kivy.uix.screenmanager import (ScreenManager, Screen, FadeTransition)
from kivy.uix.button import Button
# from kivy.uix.widget import Widget
from kivy.uix.label import Label

from kivy.core.window import Window

Window.clearcolor = (1, 1, 1, 1)


class AcquaiNoteApp(App):  # create subclass of a kivy class
    def build(self):
        # label = Label(
        #     text="AcquaiNote",
        #     font_size='20sp',
        #     bold=True,
        #     italic=True,
        #     color="#6A5ACD"
        # )
        button = Button(
            text="+",
            font_size="20sp",
            pos_hint={'center_x': 0.5, 'center_y': 0.1},
            size=(50, 50),
            size_hint=(0.15, 0.15),
            on_press=self.printpress,
            on_release=self.printrelease
        )
        return button

    def printpress(self, obj):
        print("Button has been pressed")

    def printrelease(self, obj):
        print("Button has been released")


if __name__ == '__main__':
    AcquaiNoteApp().run()
