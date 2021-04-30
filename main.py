import os
import sys

# from kivy.app import App

from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.button import MDFloatingActionButton, MDFlatButton, MDRectangleFlatButton, MDIconButton
from kivymd.uix.screen import Screen
from kivymd.uix.textfield import MDTextField
from kivymd.font_definitions import theme_font_styles

# from kivymd.theming import ThemeManager
# from kivymd.navigationdrawer import NavigationDrawer

# from kivy.uix.screenmanager import (ScreenManager, Screen, FadeTransition)

from kivy.uix.widget import Widget

from kivy.uix.image import Image, AsyncImage
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

from kivy.core.window import Window

from kivy.lang import Builder

Window.clearcolor = (1, 1, 1, 1)
Window.size = (360, 600)

username_helper = """
MDTextField:
    hint_text: "Enter username"
    icon_right: "account"
    icon_right_color: app.theme_cls.primary_color
    size_hint: (300, None)
    width: 300
    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
"""
password_helper = """
MDTextField:
    hint_text: "Enter password"
    size_hint: (300, None)
    width: 300
    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
"""

class AcquaiNoteApp(MDApp):  # create subclass of a kivy class

    def build(self):
        self.theme_cls.primary_palette = "Indigo"
        self.theme_cls.primary_hue = "500"
        self.theme_cls.theme_style = "Light"
        screen = Screen()
        layout = BoxLayout(
            orientation='vertical',
            spacing=10,
            padding=70
        )
        label = MDLabel(
            text="AcquaiNote",
            theme_text_color='Custom',
            text_color=(0.4, 0.4, 0.8, 1),
            font_style='H4',
            halign='center',
            italic=True
        )
        img = Image(
            source='data/images/contact_image_b.png'
        )
        login_layout = GridLayout(
            cols=1,
            row_force_default=True,
            row_default_height=40
        )
        self.username_fld = Builder.load_string(username_helper)
        self.password_fld = Builder.load_string(password_helper)

        login_layout.add_widget(self.username_fld)
        login_layout.add_widget(self.password_fld)

        login_btn = MDRectangleFlatButton(
            text="Login",
            size_hint=(None, None),
            width=180,
            height=50,
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            on_press=self.login
        )
        layout.add_widget(label)
        layout.add_widget(img)
        layout.add_widget(login_layout)
        layout.add_widget(login_btn)

        screen.add_widget(layout)
        return screen

    def login(self, obj):
        print("username:" + self.username_fld.text)
        print("password:" + self.password_fld.text)


if __name__ == '__main__':
    AcquaiNoteApp().run()
