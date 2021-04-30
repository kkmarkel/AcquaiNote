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

# from kivy.lang import Builder
#
# from kivy.animation import Animation
#
# from kivy.config import ConfigParser
#
# from kivy.clock import Clock, _default_time
#
# from kivy.properties import ObjectProperty, DictProperty
#
# from libs.uix import customsettings
# from libs.uix.dialogs import dialog
# from libs.uix.startscreen import StartScreen
#
# from libs import programdata as data
# from libs import programclass as _class


# class MainScreen(Widget):
#     pass


class AcquaiNoteApp(App):       # create subclass of a kivy class
    def build(self):
        label = Label(
            text="AcquaiNote",
            font_size='20sp',
            bold=True,
            italic=True
        )
        return label


if __name__ == '__main__':
    AcquaiNoteApp().run()

