from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen

#Define our different screens
class FirstWindow(Screen):
    pass

class SecondWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass


#kv = Builder.load_file('window.kv')


class WindowApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file('window.kv')
        
        

WindowApp().run()
