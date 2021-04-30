from kivy.app import App
from kivy.uix.button import Button


class FunkyButton(Button):
    def __init__(self, **kwargs):
        super(FunkyButton, self).__init__(**kwargs)
        self.text = "hello world"
        self.pos = (100, 100)
        self.size_hint = (0.25, 0.25)


class AcquaiNoteApp(App):       # create subclass of a kivy class
    def build(self):
        return FunkyButton()


if __name__ == '__main__':
    AcquaiNoteApp().run()

