# 9.13 Modifique o teclado de telefone GUI da Seção 9.1 de modo que tenha botões em vez de dígitos.
# Quando o usuário disca um número, os dígitos do número devem ser exibidos no shell interativo.

from tkinter import Tk, Label, Button, RAISED, TOP
from tkinter.messagebox import showinfo

def digitaNumero(numero):
    global numeroPrevio
    if numero == 'Apagar':
        numeroPrevio = numeroPrevio[0:len(numeroPrevio)-1]
        telefone.configure(text=numeroPrevio)
        return
    if numero == 'Apagar Tudo':
        numeroPrevio = ""
        telefone.configure(text=numeroPrevio)
        return
    if len(numeroPrevio) > 9:
        showinfo("Não há mais espaço para preencher")
        return
    numeroPrevio += numero
    telefone.configure(text=numeroPrevio)

raiz = Tk()
raiz.title("Telefone")

numeroPrevio = ""
telefone = Label(raiz, text=numeroPrevio, font=('Arial', 20), width=15, height=2, relief=RAISED, anchor='center')
telefone.grid(row=0, column=0, columnspan=3, padx=5, pady=5)

labels = [['1', '2', '3'],
          ['4', '5', '6'],
          ['7', '8', '9'],
          ['*', '0', '#'],
          ['Apagar'],
          ['Apagar Tudo']]

for r in range(len(labels)):
    for c in range(len(labels[r])):
        if labels[r][c] == 'Apagar':
            label = Button(raiz,
                      text=labels[r][c],
                      font=('Arial', 12),
                      width=7,
                      height=2,
                      relief=RAISED,
                      command=lambda x=labels[r][c]: digitaNumero(x))
            label.grid(row=r+1, column=c+1,columnspan=3, padx=5, pady=5)
        elif labels[r][c] == 'Apagar Tudo':
            label = Button(raiz,
                      text=labels[r][c],
                      font=('Arial', 12),
                      width=7,
                      height=2,
                      relief=RAISED,
                      command=lambda x=labels[r][c]: digitaNumero(x))
            label.grid(row=r+1, column=c+1,columnspan=3, padx=5, pady=5)
        else:
            label = Button(raiz,
                        text=labels[r][c],
                        font=('Arial', 12),
                        width=7,
                        height=2,
                        relief=RAISED,
                        command=lambda x=labels[r][c]: digitaNumero(x))
            label.grid(row=r+1, column=c+1, padx=5, pady=5)

raiz.mainloop()
