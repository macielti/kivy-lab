from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.storage.jsonstore import JsonStore
from os.path import join
import os



class Tela(BoxLayout):
    def gerar_arqv(self):
        app_folder = os.path.dirname(os.path.abspath(__file__))
        with open(app_folder + "/test.txt", "w") as file:
            file.write("\nBruno, testando.\n")
            
             

            
    


class Teste(App):
    def build(self):
        
        return Tela()

if __name__ == "__main__":
    Teste().run()

