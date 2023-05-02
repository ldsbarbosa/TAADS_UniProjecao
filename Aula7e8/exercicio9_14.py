# 9.14 No programa plotter.py, o usuário precisa clicar em um dos quatro botões para mover a caneta.
# Modifique o programa para permitir que o usuário utilize as teclas de seta no teclado em vez disso.

from tkinter import Tk, Canvas, Frame, Button, SUNKEN, LEFT, RIGHT


def up(event=None):
    'move caneta 10 pixels para cima'
    global y, canvas    # y é modificado

    canvas.create_line(x, y, x, y-10, fill='blue', width=2)
    y -= 10

def down(event=None):
    'move caneta 10 pixels para baixo'
    global y, canvas    # y é modificado

    canvas.create_line(x, y, x, y+10, fill='red', width=2)
    y += 10

def right(event=None):
    'move caneta 10 pixels para direita'
    global x, canvas    # x é modificado

    canvas.create_line(x, y, x+10, y, fill='green', width=2)
    x += 10

def left(event=None):
    'move caneta 10 pixels para esquerda'
    global x, canvas    # x é modificado

    canvas.create_line(x, y, x-10, y, fill='purple', width=2)
    x -= 10

def on_key_press(event):
    'chamada quando uma tecla for pressionada'
    if event.keysym == 'Up':
        up()
    elif event.keysym == 'Down':
        down()
    elif event.keysym == 'Left':
        left()
    elif event.keysym == 'Right':
        right()
    elif event.keysym == 'BackSpace':
        reset()

def reset():
    'apaga a linha e reinicia x e y'
    global x, y
    canvas.delete('all')
    x, y = 50, 75


raiz = Tk()

canvas = Canvas(raiz, height=100, width=150,
                relief=SUNKEN, borderwidth=3, bg='white')
canvas.pack(side=LEFT)

box = Frame(raiz, bg='white')
box.pack(side=RIGHT)

button = Button(box, text='up', command=up, bg='blue', fg='white')
button.grid(row=0, column=0, columnspan=2)

button = Button(box, text='left', command=left, bg='purple', fg='white')
button.grid(row=1, column=0)

button = Button(box, text='right', command=right, bg='green', fg='white')
button.grid(row=1, column=1)

button = Button(box, text='down', command=down, bg='red', fg='white')
button.grid(row=2, column=0, columnspan=2)

button = Button(box, text='reset', command=reset, bg='gray', fg='white')
button.grid(row=3, column=0, columnspan=2)

x, y = 50, 75

# vincula as teclas de seta ao método on_key_press
canvas.bind('<Up>', on_key_press)
canvas.bind('<Down>', on_key_press)
canvas.bind('<Left>', on_key_press)
canvas.bind('<Right>', on_key_press)
canvas.bind('<BackSpace>', on_key_press)

canvas.focus_set()  # faz o canvas receber o foco

raiz.mainloop()
