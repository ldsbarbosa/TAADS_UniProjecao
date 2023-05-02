from tkinter import Tk, Canvas
from tkinter.messagebox import showinfo

def iniciar_curva(event):
    'inicializa o início da curva com a posição do mouse '

    global x_antigo, y_antigo, segmentos_curva
    x_antigo, y_antigo = event.x, event.y
    segmentos_curva = []  # armazena os segmentos da curva atual


def desenhar_curva(event):
    'desenha um segmento de linha da posição antiga do mouse à nova'

    global x_antigo, y_antigo, canvas, segmentos_curva
    x_novo, y_novo = event.x, event.y
    segmentos_curva.append(canvas.create_line(
        x_antigo, y_antigo, x_novo, y_novo))
    x_antigo, y_antigo = x_novo, y_novo


def excluir_ultima_curva(event):
    'exclui a última curva desenhada'

    global segmentos_curva
    if event.keysym == 'Control_L':
        # exclui todos os segmentos da última curva
        for segmento in segmentos_curva:
            canvas.delete(segmento)
        # remove a última curva da lista de curvas
        segmentos_curva = segmentos_curva[:-1]


raiz = Tk()

x_antigo, y_antigo = 0, 0  # coordenadas do mouse (variáveis globais)
segmentos_curva = []  # armazena os segmentos da curva atual
canvas = Canvas(raiz, height=100, width=150)
canvas.bind("<Button-1>", iniciar_curva)
canvas.bind("<Button1-Motion>", desenhar_curva)
# vincula o evento Ctrl + clique do botão esquerdo à função excluir_ultima_curva()
canvas.bind("<Control-Button-1>", excluir_ultima_curva)
canvas.pack()

raiz.mainloop()
