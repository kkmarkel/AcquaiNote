from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget


class MainScreen(Widget):
    pass


class AcquaiNoteApp(App):       # create subclass of a kivy class
    def build(self):
        return MainScreen()


if __name__ == '__main__':
    AcquaiNoteApp().run()

