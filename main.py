from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class MainWidget(GridLayout):
    pass
 
# we are defining the Base Class of our Kivy App
class MathApp(App):
    def build(self):
        # return a MainWidget() as a root widget
        return MainWidget()

if __name__ == '__main__':
    MathApp().run()