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

from kivy.uix.screenmanager import (ScreenManager, Screen, FadeTransition)

from kivy.uix.widget import Widget

from kivy.uix.image import Image, AsyncImage
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

from kivy.core.window import Window

from kivy.lang import Builder

# from kivy.properties import ObjectProperty, StringProperty

from data.builder import username_field_config


class LoginScreen(Screen):
    pass


class MainScreen(Screen):
    pass


class ProfileScreen(Screen):
    pass


class WindowManager(ScreenManager):
    def login(self):
       print("It works")


class AcquaiNoteApp(MDApp):  # create subclass of a kivymd class
    # sm = ScreenManager()
    # sm.add_widget(LoginScreen(name='login_screen'))
    # sm.add_widget(MainScreen(name='main_screen'))
    # sm.add_widget(ProfileScreen(name='profile_screen'))
    Window.clearcolor = (1, 1, 1, 1)
    Window.size = (360, 640)

    # BUILDER FUNCTION AND SCREEN

    def build(self):
        screen = Screen()

        # theme settings
        self.theme_cls.primary_palette = "Indigo"
        self.theme_cls.primary_hue = "500"
        self.theme_cls.theme_style = "Light"
        # end of theme declaration
        
        kv = Builder.load_file('data/screen_helper.kv')
        return kv

    def login(self, obj):
        print("It works")

    # def build(self):
    #     screen = Screen()
    #     self.username_field = Builder.load_string(username_field_config)
    #     login_button = MDRectangleFlatButton(
    #         text="Login",
    #         size_hint=(None, None),
    #         width=180,
    #         height=50,
    #         pos_hint={'center_x': 0.5, 'center_y': 0.4},
    #         on_press=self.login
    #     )
    #     screen.add_widget(self.username_field)
    #     screen.add_widget(login_button)
    #     return screen
    #
    # def login(self, obj):
    #     print(self.username_field.text)
    #
    # #    print("username:" + self.username_fld.text)
    # #    print("password:" + self.password_fld.text)
    #
    # def add_contact(self, obj):
    #     pass


if __name__ == '__main__':
    AcquaiNoteApp().run()
