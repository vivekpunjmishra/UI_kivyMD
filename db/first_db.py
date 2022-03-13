from kivy.lang import Builder
from kivymd.app import MDApp
import sqlite3



class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"

        #Create Database or Cennect To one
        conn = sqlite3.connect('user.db')

        #Create A Cursor
        c = conn.cursor()

        c.execute("""CREATE TABLE if not exists user(
            name text,
            password text) 
        """)
        # Commit our chanes
        conn.commit()

        #Close our connection
        conn.close()

        return Builder.load_file('first_db.kv')
        
    def submit(self):
        #Create Database or Cennect To one
        conn = sqlite3.connect('user.db')

        #Create A Cursor
        c = conn.cursor()

        #Add A Record 
        c.execute("INSERT INTO user VALUES (:first),(:password)",
        {
            'first':self.root.ids.word_input.text,
            'password':self.root.ids.password.text
        })
        #Add a little message
        self.root.ids.word_label.text = f'{ self.root.ids.word_input.text}Added'

        #Clear the input box
        self.root.ids.word_input.text=''

        # Commit our chanes
        conn.commit()

        #Close our connection
        conn.close()

    def show_records(self):
        
        #Create Database or Cennect To one
        conn = sqlite3.connect('user.db')

        #Create A Cursor
        c = conn.cursor()

        #Grab record from database
        c.execute("SELECT * FROM user")
        records = c.fetchall()

        word = ''

        #loop thru records
        for record in records:
            word =f'{word}\n{record[0]}'
            self.root.ids.word_label.text =f'{word}'


        # Commit our chanes
        conn.commit()

        #Close our connection
        conn.close()

MainApp().run()
