from kivy.app import App
from kivy.uix.button import Button


class AcquaiNoteApp(App):       # create subclass of a kivy class
    def build(self):
        return Button(
            text="Hello World!",
            pos=(50,50),
            size=(500,500),
            size_hint=(0.8,0.8))      # a button with a specific size


if __name__ == '__main__':
    AcquaiNoteApp().run()

