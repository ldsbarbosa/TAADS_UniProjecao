from tkinter import Button, Entry, Frame, Tk, font, RIDGE, RAISED
from math import sqrt


class Calculadora(Frame):
    def __init__(self, master):
        'Construtor da calculadora'
        Frame.__init__(self, master)
        self.pack()

        # Alterações de estilo
        self.fonte = font.Font(family='Helvetica', size=18, weight='bold')
        self.bg_botao_igual = '#EEB422'
        self.width_borda_botao = 3

        self.memory = ''
        self.expr = ''
        self.start_of_next_operand = True

        self.botoes = [
            ['MC', 'M+', 'M-', 'MR'],
            ['C', '\u221a', 'x\u00b2', '+'],
            ['7', '8', '9', '-'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '/'],
            ['0', '.', '+-', '=']
        ]

        self.entry = Entry(self, relief=RIDGE, borderwidth=3,
                           width=20, bg='gray',
                           font=self.fonte)
        self.entry.grid(row=0, column=0, columnspan=5)

        for r in range(6):
            for c in range(4):
                def cmd(x=self.botoes[r][c]):
                    self.click(x)
                b = Button(self,
                           text=self.botoes[r][c],
                           width=3,
                           relief=RAISED,
                           font=self.fonte,
                           bg=self.bg_botao_igual if self.botoes[r][c] == '=' else 'white',
                           bd=self.width_borda_botao,
                           command=cmd)
                b.grid(row=r+1, column=c)

    def click(self, key):
        if key == '=':
            try:
                result = eval(self.expr + self.entry.get())
                self.entry.delete(0, 'end')
                self.entry.insert('end', result)
                self.expr = ''
            except:
                self.entry.delete(0, 'end')
                self.entry.insert('end', 'Error')
        elif key in '+*-/':
            self.expr += self.entry.get()
            self.expr += key
            self.start_of_next_operand = True
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
            self.entry.delete(0, 'end')
            self.entry.insert('end', result)
        elif key == 'x\u00b2':
            result = eval(self.entry.get())**2
            self.entry.delete(0, 'end')
            self.entry.insert('end', result)
        elif key == 'C':
            self.entry.delete(0, 'end')
        elif key in {'M+', 'M-'}:
            self.memory = str(eval(self.memory+key[1]+self.entry.get()))
        elif key == 'MR':
            self.entry.delete(0, 'end')
            self.entry.insert('end', self.memory)
        elif key == 'MC':
            self.memory = ''
        else:
            if self.start_of_next_operand:
                self.entry.delete(0, 'end')
                self.start_of_next_operand = False
            self.entry.insert('end', key)


raiz = Tk()
raiz.configure(bg='gray')
calculadora = Calculadora(raiz)
raiz.mainloop()
