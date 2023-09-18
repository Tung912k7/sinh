from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.utils import platform


class MainScreen(Screen):
    pass


class SecondScreen(Screen):
    pass


class Second1Screen(Screen):
    pass


class Second2Screen(Screen):
    pass


class ThirdScreen(Screen):
    pass


class Third1Screen(Screen):
    pass


class Third2Screen(Screen):
    pass


class Third11Screen(Screen):
    pass


class Third12Screen(Screen):
    pass


class Third13Screen(Screen):
    pass


class FourthScreen(Screen):
    pass


class Fourth1Screen(Screen):
    pass


class Fourth2Screen(Screen):
    pass


class Fourth3Screen(Screen):
    pass


class FifthScreen(Screen):
    pass


class Fifth1Screen(Screen):
    pass


class Fifth2Screen(Screen):
    pass


class Fifth3Screen(Screen):
    pass


class Fifth4Screen(Screen):
    pass


class App(MDApp):
    def build(self):
        self.icon = "images/icon.png"
        if platform == "android" or platform == "win" or platform == "linux":
            Window.maximize()
        else:
            Window.size = (480, 800)
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Indigo"
        self.theme_cls.accent_palette = "Red"
        screen = Screen()
        screen = Builder.load_file("mdmain - Copy.kv")
        return screen


App().run()
