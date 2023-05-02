from tkinter.messagebox import showinfo
from time import strptime, strftime
from tkinter import Tk, Button, Entry, Label, END

def compute():
    '''exibe dia da semana correspondente à data em dateEnt
    data deve ter formato MMM DD, AAAA (ex.: Jan 21, 1967)'''

    global dateEnt # dateEnt é uma variável global
    date = dateEnt.get()
    weekday = strftime('%A', strptime(date, '%b %d, %Y'))
    showinfo(message='{} foi {}'.format(date, weekday))
    dateEnt.delete(0, END)

raiz = Tk()

label = Label(raiz, text='Digite a data')
label.grid(row=0, column=0)

dateEnt = Entry(raiz)
dateEnt.grid(row=0, column=1)

button = Button(raiz, text='Entrar', command=compute)
button.grid(row=1, column=0, columnspan=2)

raiz.mainloop()