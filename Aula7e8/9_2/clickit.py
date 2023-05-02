from tkinter import Tk, Button
from tkinter.messagebox import showinfo
from time import strftime, localtime
def clicked():
    'exibe informação de dia e hora'
    hora = strftime('Dia: %d %b %Y\nHora: %H:%M:%S %p\n',localtime())
    # print(hora)
    showinfo(message=hora)

raiz = Tk()
button = Button(raiz,
    text='Clique aqui',
    command=clicked)
button.pack()
raiz.mainloop()
    