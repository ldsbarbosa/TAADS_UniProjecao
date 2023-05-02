from time import strptime, strftime
from tkinter import Tk, Button, Entry, Label, END
import locale

locale.setlocale(locale.LC_TIME, 'pt_BR.utf8')

def calcular():
    '''exibe dia da semana correspondente à data em dateEnt
    data deve ter formato MMM DD, AAAA (ex.: Jan 21, 1967)'''
    global dateEnt
    date = dateEnt.get()
    dt = strptime(date, '%d de %B de %Y')
    data_formatada = strftime('%A, %d de %B de %Y', dt)
    dateEnt.delete(0, END)
    dateEnt.insert(0, data_formatada)

def apagar():
    dateEnt.delete(0, END)

raiz = Tk()

label = Label(raiz, text='Digite a data')
label.grid(row=0, column=0)

dateEnt = Entry(raiz)
dateEnt.grid(row=0, column=1)

button = Button(raiz, text='Calcular', command=calcular)
button.grid(row=1, column=0, columnspan=1)

button = Button(raiz, text='Apagar', command=apagar)
button.grid(row=1, column=3, columnspan=1)

raiz.mainloop()