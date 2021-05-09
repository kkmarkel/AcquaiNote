import os
import sys
import sqlite3

# from kivy.app import App

from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.button import MDFloatingActionButton, MDFlatButton, MDRectangleFlatButton, MDIconButton

from kivymd.uix.textfield import MDTextField
from kivymd.uix.list import MDList, OneLineListItem
from kivymd.uix.picker import MDThemePicker
from kivymd.font_definitions import theme_font_styles

# from kivymd.theming import ThemeManager
# from kivymd.navigationdrawer import NavigationDrawer

from kivy.uix.popup import Popup
from kivy.uix.screenmanager import (ScreenManager, Screen, FadeTransition)

from kivy.uix.widget import Widget

from kivy.uix.image import Image, AsyncImage
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

from kivy.core.window import Window

from kivy.lang import Builder
from kivy.clock import Clock

# from kivy.properties import ObjectProperty, StringProperty



# calling of screen classes and addition to the screen_manager

class LoadingScreen(Screen):
    def __init__(self, **kwargs):
        super(LoadingScreen, self).__init__(**kwargs)
        Clock.schedule_once(self.callNext, 7)

    def callNext(self, dt):
        self.manager.current = 'home_screen'


class HomeScreen(Screen):
    pass


class RoomScreen(Screen):
    pass


class SettingsScreen(Screen):
    pass


class ProfileScreen(Screen):
    pass


# class ScreenManager(ScreenManager):
#     pass
#     # def login(self):
#     #     print("It works")

manager = ScreenManager()
manager.add_widget(HomeScreen(name='home_screen'))
manager.add_widget(LoadingScreen(name='loading_screen'))
manager.add_widget(RoomScreen(name='room_screen'))
manager.add_widget(SettingsScreen(name='settings_screen'))

# end of call of screen classes and addition to screenmanager


class AcquaiNoteApp(MDApp):  # create subclass of a kivymd class
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    # sm = ScreenManager()
    # sm.add_widget(LoginScreen(name='login_screen'))
    # sm.add_widget(MainScreen(name='main_screen'))
    # sm.add_widget(ProfileScreen(name='profile_screen'))
    # Window.clearcolor = (1, 1, 1, 1)
    Window.size = (360, 640)

    # -------------------------- CODE FOR THE DATABASE ---------------------------------- #
    conn = sqlite3.connect('acquai_database.db')
    cursor = conn.cursor()

    # cursor.execute('''CREATE TABLE users (
    #                 email text,
    #                 password integer
    #                 )''')

    def sign_up(self, cursor):
        cursor.execute('INSERT INTO users VALUES('', '')')

    conn.commit()
    conn.close()

    # -------------------------- END OF CODE FOR THE DATABASE ---------------------------------- #

    # BUILDER FUNCTION AND SCREEN

    def build(self):
        screen = Screen()

        # theme settings
        self.theme_cls.primary_palette = "Indigo"
        self.theme_cls.primary_hue = "500"
        self.theme_cls.theme_style = "Light"
        # end of theme declaration

        # loaded strings
        configuration = Builder.load_file(
            'data/screen_helper.kv')  # saving a reference to the loaded ScreenManager
        # end of loaded strings

        # addition of loaded strings to screen + return screen
        screen.add_widget(configuration)

        return screen
        # end of addition

    # END OF BUILDER FUNCTION

    # USER VALIDATION FUNCTION (with a password?)

    # def login(self):
    #     email_addr = self.configuration.get_screen('loading_screen').ids.email.text

    #     if email_addr == str(''):
    #         print("Invalid Email Address")

    # END OF USER VALIDATION

    def change(self, dt):
        self.root.manager.current = 'home'

    # App theme manager
    def change_theme(self):
        if self.theme_cls.theme_style == "Light":
            self.theme_cls.theme_style = "Dark"
        elif self.theme_cls.theme_style == "Dark":
            self.theme_cls.theme_style = "Light"
        else:
            pass

        # theme_dialog = MDThemePicker()
        # theme_dialog.open()       # почему-то не работает :(

    # End of app theme manager

    # home page search bar
    def search_bar(self, dt):
        searchbar = Popup(
            title='Search',
            content=MDTextField(
                helper_text='Input values to be searched for',
                helper_text_mode='on_focus'
            ),
            auto_dismiss=True,
            # size_hint=(None, None),
            # size=(400, 98)
            size_hint=(0.7, 0.17),
            pos_hint={'center_x': 0.5, 'center_y': 0.8}
        )
        searchbar.open()

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


# APP RUN
if __name__ == '__main__':
    AcquaiNoteApp().run()
