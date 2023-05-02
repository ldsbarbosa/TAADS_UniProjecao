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

        self.buttonUp = Button(self.box, text='up', command=self.up)
        self.buttonUp.grid(row=0, column=0, columnspan=2)

        self.buttonLeft = Button(self.box, text='left', command=self.left)
        self.buttonLeft.grid(row=1, column=0)

        self.buttonRight = Button(self.box, text='right', command=self.right)
        self.buttonRight.grid(row=1, column=1)

        self.buttonDown = Button(self.box, text='down', command=self.down)
        self.buttonDown.grid(row=2, column=0, columnspan=2)

        self.x, self.y = 50, 75

    def up(self):
        'move caneta 10 pixels para cima'
        self.y, self.canvas    # y é modificado

        self.canvas.create_line(self.x, self.y, self.x, self.y-10)
        self.y -= 10

    def down(self):
        'move caneta 10 pixels para baixo'
        self.y, self.canvas    # y é modificado

        self.canvas.create_line(self.x, self.y, self.x, self.y+10)
        self.y += 10

    def right(self):
        'move caneta 10 pixels para direita'
        self.x, self.canvas    # x é modificado

        self.canvas.create_line(self.x, self.y, self.x, self.x+10)
        self.x += 10

    def left(self):
        'move caneta 10 pixels para esquerda'
        self.x, self.canvas    # x é modificado

        self.canvas.create_line(self.x, self.y, self.x, self.x-10)
        self.x -= 10


raiz = Tk()

plotter = Plotter(raiz)
raiz.mainloop()
