from time import strftime, localtime
from tkinter.messagebox import showinfo
from tkinter import Button, Frame


class ClickIt(Frame):
    'GUI que apresenta hora atual'

    def __init__(self, master):
        'construtor'
        Frame.__init__(self, master)
        self.pack()
        button = Button(self,
                        text='Clique aqui',
                        command=self.clicked)
        button.pack()

    def clicked(self):
        'apresenta informações de dia e hora'
        time = strftime('Dia: %d %b %Y\nHora: %H:%M:%S %p\n',
                        localtime())
        showinfo(message=time)
