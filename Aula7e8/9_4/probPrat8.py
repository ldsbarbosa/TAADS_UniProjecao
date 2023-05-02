from tkinter import Tk, Text, BOTH, Frame

class KeyLogger(Frame):
    def __init__(self, master=None): # Construtor
        super().__init__(master) # Construtor do pai
        self.text = Text(self, width=20, height=5) # Define, a si mesma, um atributo
        # O atributo chama-se text, que é a instanciação de Text().
        self.text.bind('<KeyPress>', self.record)
        # Dá um bind no atributo text para relacionar um evento, chamando um método
        # da propria classe
        self.text.pack(expand=True, fill=BOTH)
        # Por fim, o pack é para empacotar no Frame, e o Frame vai empacotar no Tk(), que é a tela.

    def record(self, event):
        '''função de manipulação de evento para evento de tecla pressionada
        evento de entrada é do tipo tkinter.Event '''
        print('char = {}'.format(event.keysym)) # exibe símbolo da tecla

raiz = Tk()
app = KeyLogger(raiz)
app.pack(expand=True, fill=BOTH)
raiz.mainloop()
