from tkinter import Canvas, Frame, BOTH

class Draw(Frame):
    'uma aplicação de desenho básica'
    
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.pack()

        # coordenadas do mouse são variáveis de instância
        self.oldx, self.oldy = 0, 0

        # cria tela e vincula eventos do mouse aos manipuladores
        self.canvas = Canvas(self, height=100, width=150)
        self.canvas.bind("<Button -1>", self.begin)
        self.canvas.bind("<Button1 -Motion>", self.draw)
        self.canvas.pack(expand=True, fill=BOTH)
        
        def begin(self, event):
            'trata clique do botão esquerdo registrando posição do mouse'
            self.oldx, self.oldy = event.x, event.y

        def draw(self, event):
            '''trata movimento do mouse, ao pressionar botão esquerdo,
            conectando posição anterior à nova posição do mouse '''
            newx, newy = event.x, event.y
            self.canvas.create_line(self.oldx, self.oldy, newx, newy)
            self.oldx, self.oldy = newx, newy
