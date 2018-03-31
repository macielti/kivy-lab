from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class Tela(BoxLayout):
    def gerar_arqv(self):
        with open("test.txt", "w") as file:
            file.write("\nBruno, testando.\n")
    


class Teste(App):
    def build(self):
        return Tela()

if __name__ == "__main__":
    Teste().run()

