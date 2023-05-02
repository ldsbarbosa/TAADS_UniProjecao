from tkinter import Tk, Button
from tkinter.messagebox import showinfo
from time import strftime, localtime, gmtime
def horaLocal():
    'exibe informação de dia e hora'
    hora = strftime('Dia: %d %b %Y\nHora: %H:%M:%S %p\n',localtime())
    showinfo(message=hora)

def horaGreenwich():
    'exibe informação de dia e hora de acordo com Greenwich'
    hora = strftime('Dia: %d %b %Y\nHora: %H:%M:%S %p\n',gmtime())
    showinfo(message=hora)
    return 0

raiz = Tk()
botaoLocal = Button(raiz,text="Hora Local",command=horaLocal)
botaoLocal.pack()

botaoGreenwich = Button(raiz,text="Hora Greenwitch",command=horaGreenwich)
botaoGreenwich.pack()
raiz.mainloop()