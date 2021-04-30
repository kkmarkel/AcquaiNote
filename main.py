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
Window.size = (360, 600)


class AcquaiNoteApp(App):  # create subclass of a kivy class
    def build(self):
        layout = BoxLayout(
            orientation='vertical',
            spacing=100,
            padding=80
        )
        img = Image(
            source='data/images/contact_image_b.png'
        )
        button = Button(
            text="Login",
            size_hint=(None, None),
            width=180,
            height=50,
            pos_hint={'center_x': 0.5}
        )
        layout.add_widget(img)
        layout.add_widget(button)
        return layout


if __name__ == '__main__':
    AcquaiNoteApp().run()
