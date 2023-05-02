# 9.16 Acrescente mais dois botões ao widget Plotter.
# Um, rotulado “apagar”, deverá apagar a tela. O outro, rotulado “excluir”,
# deverá apagar o último movimento da caneta.

from tkinter import Tk, Canvas, Frame, Button, SUNKEN, LEFT, RIGHT

class Plotter(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.pack()

        self.canvas = Canvas(master, height=100, width=150, relief=SUNKEN, borderwidth=3)
        self.canvas.pack(side=LEFT)

        self.box = Frame(master)
        self.box.pack(side=LEFT)

        self.buttonUp = Button(self.box, text='cima', command=lambda: self.move(0, -10))
        self.buttonUp.grid(row=0, columnspan=2)

        self.buttonLeft = Button(self.box, text='esquerda', command=lambda: self.move(-10, 0))
        self.buttonLeft.grid(row=1, column=0)

        self.buttonRight = Button(self.box, text='direita', command=lambda: self.move(10, 0))
        self.buttonRight.grid(row=1, column=1)

        self.buttonDown = Button(self.box, text='baixo', command=lambda: self.move(0, 10))
        self.buttonDown.grid(row=2, columnspan=2)

        self.buttonClear = Button(self.box, text='apagar', command=self.clear_canvas)
        self.buttonClear.grid(row=3, columnspan=2)

        self.buttonUndo = Button(self.box, text='excluir', command=self.undo_move)
        self.buttonUndo.grid(row=4, columnspan=2)

        self.x, self.y = 50, 75
        self.moves = []

    def move(self, dx, dy):
        'move caneta dx pixels para direita e dy pixels para baixo'
        self.canvas.create_line(self.x, self.y, self.x+dx, self.y+dy)
        self.moves.append((dx, dy))
        self.x += dx
        self.y += dy

    def clear_canvas(self):
        'apaga a tela'
        self.canvas.delete("all")
        self.moves = []
        self.x, self.y = 50, 75

    def undo_move(self):
        'apaga o último movimento da caneta'
        if self.moves:
            dx, dy = self.moves.pop()
            self.canvas.create_line(self.x, self.y, self.x-dx, self.y-dy, fill=self.canvas["bg"], width=3)
            self.x -= dx
            self.y -= dy

root = Tk()

plotter = Plotter(root)
root.mainloop()
