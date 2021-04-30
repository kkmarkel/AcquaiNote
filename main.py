import os
import sys

# from kivy.app import App

from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.button import MDFloatingActionButton, MDFlatButton
from kivymd.uix.screen import Screen
from kivymd.font_definitions import theme_font_styles

# from kivymd.theming import ThemeManager
# from kivymd.navigationdrawer import NavigationDrawer

# from kivy.uix.screenmanager import (ScreenManager, Screen, FadeTransition)
from kivy.uix.button import Button
from kivy.uix.widget import Widget

from kivy.uix.image import Image, AsyncImage
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

from kivy.core.window import Window

Window.clearcolor = (1, 1, 1, 1)
Window.size = (360, 600)


class AcquaiNoteApp(MDApp):  # create subclass of a kivy class
    def build(self):
        layout = BoxLayout(
            orientation='vertical',
            spacing=10,
            padding=80
        )
        label = MDLabel(
            text="AcquaiNote",
            theme_text_color='Custom',
            text_color=(0.416, 0.353, 0.804, 1),
            font_style='H4',
            halign='center'
        )
        img = Image(
            source='data/images/contact_image_b.png'
        )
        login_layout = GridLayout(
            cols=1,
            row_force_default=True,
            row_default_height=40
        )
        self.login_inpt = TextInput(
            text="enter login here"
        )
        self.password_inpt = TextInput(
            text="enter password here"
        )
        login_layout.add_widget(self.login_inpt)
        login_layout.add_widget(self.password_inpt)
        login_btn = Button(
            text="Login",
            size_hint=(None, None),
            width=180,
            height=50,
            pos_hint={'center_x': 0.5},
            on_press=self.login
        )
        layout.add_widget(icon_label)
        layout.add_widget(label)
        layout.add_widget(img)
        layout.add_widget(login_layout)
        layout.add_widget(login_btn)
        return layout

    def login(self, obj):
        print("login:" + self.login_inpt.text)
        print("password:" + self.password_inpt.text)


if __name__ == '__main__':
    AcquaiNoteApp().run()
