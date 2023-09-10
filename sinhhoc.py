from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.config import Config
from kivy.utils import platform
from kivy.uix.image import Image


Config.set('graphics', 'resizable', True)
Builder.load_file('bg.kv')
class MyLayout(Image):
     pass
class MainApp(App):
    def build(self):
        if(platform == 'android'):
            Window.maximize()
        else:
            Window.size = (480,800)
        Window.clearcolor = (255,255,255,0)
        return MyLayout()

        
if __name__ == "__main__":
    MainApp().run()
