from tkinter.messagebox import showinfo
from time import strptime, strftime
from tkinter import Tk, Button, Entry, Label, END

class Day(Frame):
    'aplicação que calcula o dia da semana correspondente a uma data'

    def __init__(self, master):
        Frame.__init__(self, master)
        self.pack()

        label = Label(self, text='Digite a data')
        label.grid(row=0, column=0)

        self.dateEnt = Entry(self) # variável de instância
        self.dateEnt.grid(row=0, column=1)
        
        button = Button(self, text='Entrar',
                                command=self.compute)
        button.grid(row=1, column=0, columnspan=2)
    
    def compute(self):
        '''exibe o dia da semana que corresponde à data em dateEnt,
        no formato MMM DD, AAAA (ex.: Jan 21, 1967)'''
        date = self.dateEnt.get()
        weekday = strftime('%A', strptime(date, '%b %d, %Y'))
        showinfo(message='{} foi {}'.format(date, weekday))
        self.dateEnt.delete(0, END)
