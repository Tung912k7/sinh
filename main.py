from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.config import Config
from kivy.utils import platform
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.uix.label import Label


Config.set('graphics', 'resizable', True)

class MainWindow(Screen):
    pass

class SecondWindow(Screen, Widget):
    pass
class Second1Window(Screen):
    pass
class Second2Window(Screen):
    pass

class ThirdWindow(Screen):
    pass
class Third1Window(Screen):
    pass
class Third2Window(Screen, Widget):
    pass
class Third11Window(Screen):
    pass
class Third12Window(Screen):
    pass
class Third13Window(Screen):
    pass

class FourthWindow(Screen):
    pass
class Fourth1Window(Screen):
    pass
class Fourth2Window(Screen):
    pass 
class Fourth3Window(Screen):
    pass

class FifthWindow(Screen):
    pass
class Fifth1Window(Screen):
    pass
class Fifth2Window(Screen):
    pass
class Fifth3Window(Screen):
    pass 
class Fifth4Window(Screen):
    pass


class WindowManager(ScreenManager):
    pass

kv = Builder.load_file('main.kv')

class MainApp(App):
    def build(self):
        if(platform == 'android'):
            Window.maximize()
        else:
            Window.size = (480, 800)
        Window.clearcolor = (255, 255, 255, 0)
        return kv

        
if __name__ == "__main__":
    MainApp().run()
