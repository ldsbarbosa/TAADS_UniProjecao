# 9.15 Na implementação da classe de widget Plotter, existem quatro manipuladores de evento de botão muito semelhantes:
# up(), down(), left() e right(). Reimplemente a classe usando apenas uma função move() que aceita dois argumentos
# de entrada dx e dy e move a caneta da posição (x, y) para (x+dx, y+dx).

from tkinter import Tk, Canvas, Frame, Button, SUNKEN, LEFT, RIGHT

class Plotter(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.pack()

        self.canvas = Canvas(raiz, height=100, width=150,
                             relief=SUNKEN, borderwidth=3)
        self.canvas.pack(side=LEFT)

        self.box = Frame(raiz)
        self.box.pack(side=RIGHT)

        self.buttonUp = Button(self.box, text='up', command=lambda: self.move(0, -10))
        self.buttonUp.grid(row=0, column=0, columnspan=2)

        self.buttonLeft = Button(self.box, text='left', command=lambda: self.move(-10, 0))
        self.buttonLeft.grid(row=1, column=0)

        self.buttonRight = Button(self.box, text='right', command=lambda: self.move(10, 0))
        self.buttonRight.grid(row=1, column=1)

        self.buttonDown = Button(self.box, text='down', command=lambda: self.move(0, 10))
        self.buttonDown.grid(row=2, column=0, columnspan=2)

        self.x, self.y = 50, 75

    def move(self, dx, dy):
        'move caneta dx pixels para direita e dy pixels para baixo'
        self.canvas.create_line(self.x, self.y, self.x+dx, self.y+dy)
        self.x += dx
        self.y += dy

raiz = Tk()

plotter = Plotter(raiz)
raiz.mainloop()
