from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.storage.jsonstore import JsonStore
from random import randint



class Tela(BoxLayout):
    def gerar_arqv(self):
        number = str(randint(0,800))
        path = Teste().user_data_dir
        with open(path + "/test"+number+".txt", "w") as file:
            for i in range(0, 8000):
                file.write("\nBruno, testando.\n")
            
             

            
    


class Teste(App):
    def build(self):
        Teste().user_data_dir
        return Tela()

if __name__ == "__main__":
    Teste().run()

