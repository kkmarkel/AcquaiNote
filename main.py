import os
import sys
import sqlite3

# from kivy.app import App

from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.button import MDFloatingActionButton, MDFlatButton, MDRectangleFlatButton, MDIconButton, MDFillRoundFlatButton

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
from kivy.uix.settings import SettingsWithSidebar


from kivy.core.window import Window

from kivy.lang import Builder
from kivy.clock import Clock

from kivy.properties import ObjectProperty, StringProperty

from data.settingsjson import settings_json


# calling of screen classes and addition to the screen_manager

class LoadingScreen(Screen):
    def __init__(self, **kwargs):
        super(LoadingScreen, self).__init__(**kwargs)
        Clock.schedule_once(self.callNext, 5)

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


class NewEntryScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


manager = ScreenManager()
manager.add_widget(HomeScreen(name='home_screen'))
manager.add_widget(LoadingScreen(name='loading_screen'))
manager.add_widget(RoomScreen(name='room_screen'))
manager.add_widget(SettingsScreen(name='settings_screen'))
manager.add_widget(ProfileScreen(name='profile_screen'))
manager.add_widget(NewEntryScreen(name='new_entry_screen'))

# end of call of screen classes and addition to screenmanager


class AcquaiNoteApp(MDApp):  # create subclass of a kivymd class
    Window.size = (360, 640)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    # sm = ScreenManager()
    # sm.add_widget(LoginScreen(name='login_screen'))
    # sm.add_widget(MainScreen(name='main_screen'))
    # sm.add_widget(ProfileScreen(name='profile_screen'))
    # Window.clearcolor = (1, 1, 1, 1)

    # -------------------------- CODE FOR THE DATABASE ---------------------------------- #
    # conn = sqlite3.connect('acquai_database.db')
    # cursor = conn.cursor()

    # # cursor.execute('''CREATE TABLE users (
    # #                 email text,
    # #                 password integer
    # #                 )''')

    # def sign_up(self, cursor):
    #     cursor.execute('INSERT INTO users VALUES('', '')')

    # -------------------------- END OF CODE FOR THE DATABASE ---------------------------------- #

    # BUILDER FUNCTION AND SCREEN

    def build(self):
        screen = Screen()

        # theme settings
        self.theme_cls.primary_palette = "Indigo"
        self.theme_cls.primary_hue = "500"
        self.theme_cls.theme_style = self.config.get('Common settings', 'themesettings')
        # end of theme settings

        # loaded strings
        configuration = Builder.load_file(
            'data/screen_helper.kv')  # saving a reference to the loaded ScreenManager
        # end of loaded strings

        # addition of loaded strings to screen + return screen
        screen.add_widget(configuration)
        # end of addition

        # settings of settings
        # self.settings_cls = SettingsWithSidebar
        self.use_kivy_settings = False
        # setting = self.config.get('example', 'boolexample')

        # end of settings of settings

        return screen
        

    # END OF BUILDER FUNCTION

    # USER VALIDATION FUNCTION (with a password?)

    # def login(self):
    #     email_addr = self.configuration.get_screen('loading_screen').ids.email.text

    #     if email_addr == str(''):
    #         print("Invalid Email Address")

    # END OF USER VALIDATION

    def change(self, dt):
        self.root.manager.current = 'home_screen'

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

    def add_new_entry(self, *args):
        conn = sqlite3.connect('acquai_database.db')
        cursor = conn.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS entry_list (id INTEGER PRIMARY KEY AUTOINCREMENT;
                    email text,
                    password integer
                    )''')

        conn.commit()
        conn.close()
        # print(HomeScreen(name='home_screen').ids)
        # HomeScreen(name='home_screen').ids.home_list.add_widget(OneLineListItem(text = 'Example entry'))       # this function will write down entries to the sqlite database
        # #   I don't understand why it doesn't generate new list item on the home screen...
        # #   Maybe the screen needs to be updated somehow?
        # #   Whatever, I think I will first save entries to the database and then make the whole list...

    # APP SETTINGS BUILDER
    def build_config(self, config):
        config.setdefaults('Common settings', {
            'fontsizesettings': 15,
            'themesettings': 'Light',
            'pathsettings': '/some/path',
            'languagesettings': 'English'})

    def build_settings(self, settings):
        settings.add_json_panel('Settings', self.config, data=settings_json)

    # this method is automatically called whenever a user changes the configuration
    def on_config_change(self, config, section, key, value):
        self.theme_cls.theme_style = self.config.get('Common settings', 'themesettings')
        print(config, section, key, value)


    # END OF APP SETTINGS BUILDER
# APP RUN
if __name__ == '__main__':
    AcquaiNoteApp().run()
