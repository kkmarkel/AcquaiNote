import os
import sys

from kivy.app import App

# from kivymd.app import MDApp
# from kivymd.theming import ThemeManager
# from kivymd.navigationdrawer import NavigationDrawer

# from kivy.uix.screenmanager import (ScreenManager, Screen, FadeTransition)
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.image import Image, AsyncImage
from kivy.uix.boxlayout import BoxLayout

from kivy.core.window import Window

Window.clearcolor = (1, 1, 1, 1)


class AcquaiNoteApp(App):  # create subclass of a kivy class
    def build(self):
        layout = BoxLayout()
        btn = Button(
            text="+"
        )
        btn2 = Button(
            text="Menu"
        )
        layout.add_widget(btn)
        layout.add_widget(btn2)
        return layout


if __name__ == '__main__':
    AcquaiNoteApp().run()
