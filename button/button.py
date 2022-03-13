from kivy.lang import Builder
from kivymd.app import MDApp

#'Red','Pick','Purple','DeepPurple',
#'Indigo','Blue','LightBlue','Cyan',
#'Teal','Green','LightGreen','Lime',
#'Yellow','Amber','Orange','DeepOrange'
#'Brown','Gray','BlueGray'.
class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file('button.kv')
        
    def presser(self):
        self.root.ids.my_label.text = "You Pressed It!!!"        

MainApp().run()
