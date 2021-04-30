import os
import sys

from kivy.app import App

# from kivymd.app import MDApp
# from kivymd.theming import ThemeManager
# from kivymd.navigationdrawer import NavigationDrawer

# from kivy.uix.screenmanager import (ScreenManager, Screen, FadeTransition)
# from kivy.uix.button import Button
# from kivy.uix.widget import Widget
from kivy.uix.label import Label

from kivy.core.window import Window


Window.clearcolor = (1, 1, 1, 1)


class AcquaiNoteApp(App):       # create subclass of a kivy class
    def build(self):
        label = Label(
            text="AcquaiNote",
            font_size='20sp',
            bold=True,
            italic=True,
            color="#6A5ACD"
        )
        return label


if __name__ == '__main__':
    AcquaiNoteApp().run()

