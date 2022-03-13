from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window

Builder.load_file('login.kv')

class MyGridLayout(Widget):
    email = ObjectProperty(None)
    password = ObjectProperty(None)


    def press(self):
        email=self.email.text
        password=self.password.text

        #Print it to the screen
        #self.add_widget(Label(text=f"Welcome{email}Announcement messages goes here....!"))
        print(f"Welcome{email}Announcement messages goes here....!")
        #clear the input Boxes
        self.email.text=""
        self.password.password=""

class LoginApp(App):
    def build(self):
        Window.clearcolor = (1,1,1,1)
        return MyGridLayout()

if __name__=="__main__":
    LoginApp().run()

