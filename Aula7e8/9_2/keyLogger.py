from tkinter import Tk, Text, BOTH

def record(event):
    '''função de manipulação de evento para evento de tecla pressionada
    evento de entrada é do tipo tkinter.Event '''
    print('char = {}'.format(event.keysym)) # exibe símbolo da tecla

raiz = Tk()
text = Text(raiz,
            width=20,  # define largura em 20 caracteres
            height=5)  # define altura em 5 linhas de caracteres
text.bind('<KeyPress>', record)
text.pack(expand=True, fill=BOTH)
raiz.mainloop()
