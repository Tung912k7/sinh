from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.config import Config
from kivy.utils import platform
from kivy.uix.anchorlayout import AnchorLayout

Config.set('graphics', 'resizable', True)
'''Builder.load_string(""" 
<Image>
		Image:
			source: 'bg.png'
			allow_stretch: False
			keep_ratio: True
			""")'''
class MainApp(App):
    def build(self):
        if(platform == 'android'):
            Window.maximize()
        else:
            Window.size = (480,800)
        Window.clearcolor = (255,255,255,0)
        return

        
if __name__ == "__main__":
    MainApp().run()
