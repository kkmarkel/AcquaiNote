from kivy.app import App
from kivy.uix.button import Button


class FunkyButton(Button):
    pass


class AcquaiNoteApp(App):       # create subclass of a kivy class
    def build(self):
        return FunkyButton(
            pos=(100, 100),
            size_hint=(None, None),
            size=(500, 500)
        )


if __name__ == '__main__':
    AcquaiNoteApp().run()

