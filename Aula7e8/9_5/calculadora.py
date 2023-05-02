from tkinter import Button, RAISED, Entry, RIDGE, END, Frame, Tk
from math import sqrt


class Calculadora(Frame):
    def __init__(self, master):
        'Construtor da calculadora'
        Frame.__init__(self, master)
        self.pack()

        self.memory = ''
        self.expr = ''
        self.startOfNextOperand = True

        self.botoes = [['MC', 'M+', 'M-', 'MR'],
                       ['C', '\u221a', 'x\u00b2', '+'],
                       ['7', '8', '9', '-'],
                       ['4', '5', '6', '*'],
                       ['1', '2', '3', '/'],
                       ['0', '.', '+-', '=']]

        self.entry = Entry(self, relief=RIDGE, borderwidth=3,
                           width=20, bg='gray',
                           font=('Helvetica', 18))

        self.entry.grid(row=0, column=0, columnspan=5)

        for r in range(6):
            for c in range(4):
                def cmd(x=self.botoes[r][c]):
                    self.click(x)
                b = Button(self,
                           text=self.botoes[r][c],
                           width=3,
                           relief=RAISED,
                           command=cmd)
                b.grid(row=r+1, column=c)

    def click(self, key):
        'manipulador para evento de pressionar tecla rotulada do botão'
        if key == '=':
            try:
                result = eval(self.expr + self.entry.get())
                self.entry.delete(0, END)
                self.entry.insert(END, result)
                self.expr = ''
            except:
                self.entry.delete(0, END)
                self.entry.insert(END, 'Error')
        elif key in '+*-/':
            self.expr += self.entry.get()
            self.expr += key
            self.startOfNextOperand = True
        elif key == '+-':
            try:
                if self.entry.get()[0] == '-':
                    self.entry.delete(0)
                else:
                    self.entry.insert(0, '-')
            except IndexError:
                pass
        elif key == '\u221a':
            result = sqrt(eval(self.entry.get()))
            self.entry.delete(0, END)
            self.entry.insert(END, result)
        elif key == 'x\u00b2':
            result = eval(self.entry.get())**2
            self.entry.delete(0, END)
            self.entry.insert(END, result)
        elif key == 'C':
            self.entry.delete(0, END)
        elif key in {'M+', 'M-'}:
            self.memory = str(eval(self.memory+key[1]+self.entry.get()))
        elif key == 'MR':
            self.entry.delete(0, END)
            self.entry.insert(END, self.memory)
        elif key == 'MC':
            self.memory = ''
        else:
            if self.startOfNextOperand:
                self.entry.delete(0, END)
                self.startOfNextOperand = False
                self.entry.insert(END, key)


raiz = Tk()
calculadora = Calculadora(raiz)
raiz.mainloop()
