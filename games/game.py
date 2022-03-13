from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
import sqlite3

#'Red','Pick','Purple','DeepPurple',
#'Indigo','Blue','LightBlue','Cyan',
#'Teal','Green','LightGreen','Lime',
#'Yellow','Amber','Orange','DeepOrange'
#'Brown','Gray','BlueGray'.
class GameApp(MDApp):
    def games1(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "BlueGray"

        return Builder.load_file('game.kv')



GameApp().run()
