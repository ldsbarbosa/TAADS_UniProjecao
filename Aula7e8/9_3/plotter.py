from tkinter import Tk, Canvas, Frame, Button, SUNKEN, LEFT, RIGHT

def up():
    'move caneta 10 pixels para cima'
    global y, canvas    # y é modificado

    canvas.create_line(x, y, x, y-10)
    y -= 10

def down():
    'move caneta 10 pixels para baixo'
    global y, canvas    # y é modificado

    canvas.create_line(x, y, x, y+10)
    y += 10

def right():
    'move caneta 10 pixels para direita'
    global x, canvas    # x é modificado

    canvas.create_line(x, y, x, x+10)
    x += 10

def left():
    'move caneta 10 pixels para esquerda'
    global x, canvas    # x é modificado

    canvas.create_line(x, y, x, x-10)
    x -= 10

raiz = Tk()

canvas = Canvas(raiz, height=100, width=150,
                relief=SUNKEN, borderwidth=3)
canvas.pack(side=LEFT)

box = Frame(raiz)
box.pack(side=RIGHT)

button = Button(box, text='up', command=up)
button.grid(row=0, column=0, columnspan=2)

button = Button(box, text='left', command=left)
button.grid(row=1, column=0)

button = Button(box, text='right', command=right)
button.grid(row=1, column=1)

button = Button(box, text='down', command=down)
button.grid(row=2, column=0, columnspan=2)

x, y = 50, 75

raiz.mainloop()
