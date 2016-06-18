from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import StringProperty
from kivy.lang import Builder
import random

Builder.load_file('truthdare.kv')

class MainScreen(Screen):
    pass

class TruthScreen(Screen):
    """
    All the truth questions are to be here and they will be randomnized
    in the app with call from the trut button on the app
    
    """
    truths =str(random.choice(['Hello','Hi','Please']))
    
    
    def truth_words(self):
        self.truths = random.choice(['a','b','c'])
        return self.truths
        
        

class DareScreen(Screen):
    """
    ALl the dares will be in this class and will be called when the dare
    button is selected in the app. The dares will be randomnized here.
    """
    dares = str(random.choice(['me','you','him']))

sm = ScreenManager()
sm.add_widget(MainScreen(name='main'))
sm.add_widget(TruthScreen(name='truth'))
sm.add_widget(DareScreen(name='dare'))

present_screen = 0

class TruthDareApp(App):
    def build(self):
        
        return sm
    
if __name__ == "__main__":
    TruthDareApp().run()