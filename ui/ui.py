from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen

#Define our different screens
class LoginWindow(Screen):
    pass

class NotifyWindow(Screen):
    pass

class RewardsWindow(Screen):
    pass


class MailWindow(Screen):
    pass

class ChatWindow(Screen):
    pass

class PayWindow(Screen):
    pass

class SearchWindow(Screen):
    pass

class GamesWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass


class UiApp(MDApp):
    def builder(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file('ui.kv')
        
        
UiApp().run()
