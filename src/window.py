########################################################
#   MAIN WINDOW
#   TODO: Make text boxes resizable, find color theme
#
#
#
########################################################



import kivy
kivy.require('2.1.0')

from kivy.app import App # base
from kivy.config import Config # config stuff
from kivy.uix.gridlayout import GridLayout # uix
from kivy.uix.label import Label # uix
from kivy.uix.textinput import TextInput # uix
from kivy.core.window import Window # window configuration

Window.size = (1000, 550) 

class HomeScreen(GridLayout):
    def __init__(self, **kwargs):

        with open('./intro.txt', 'r') as f:
            self.txt = f.read()

        super(HomeScreen, self).__init__(**kwargs)
        self.cols = 2
        self.textOne = TextInput(text=self.txt)
        self.textTwo = TextInput()
        self.add_widget(self.textOne)
        self.add_widget(self.textTwo)
        


class NotesApp(App):

    def build(self):
        h = HomeScreen()
        return h


def run_app():
    NotesApp().run()