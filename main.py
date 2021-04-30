from kivy.app import App
from kivy.uix.button import Button


class AcquaiNoteApp(App):       # create subclass of a kivy class
    def build(self):
        return Button(
            text="Hello World!",
            pos=(50,50),
            size=(100,100))      # the whole window will be a button


if __name__ == '__main__':
    AcquaiNoteApp().run()

