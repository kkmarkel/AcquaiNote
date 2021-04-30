from kivy.app import App
from kivy.uix.button import Button


class FunkyButton(Button):
    pass


class AcquaiNoteApp(App):       # create subclass of a kivy class
    def build(self):
        return FunkyButton(
            text="hello world",
            pos=(100, 100),
            size_hint=(0.5, 0.5)
        )


if __name__ == '__main__':
    AcquaiNoteApp().run()

