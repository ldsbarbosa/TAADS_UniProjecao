# 9.11 Desenvolva um programa que exibe uma janela GUI com sua
# imagem no lado esquerdo e seu nome, sobrenome e local e data de nascimento à
# direita. A foto precisa estar no formato GIF.

# Se você não tiver uma, procure uma ferramenta conversora
# on-line gratuita e uma imagem JPEG para transformar para o formato GIF.

import tkinter
from tkinter import *
from PIL import Image, ImageTk

raiz = Tk()
raiz.config(background="#F4F4F4")

# Create a photoimage object of the image in the path
image1 = Image.open("theManWhoKnewInfinity.gif")
frames = image1.n_frames
format = f"gif -index %i"

imageObject = [ImageTk.PhotoImage(image1.copy().convert('RGBA'), format=format % i) for i in range(frames)]
count = 0

def animation():
    global count
    newImage = imageObject[count]
    label1.configure(image=newImage)
    count += 1
    if count == frames:
        count = 0
    raiz.after(200, animation)

label1 = tkinter.Label(raiz, image="", bg="#F4F4F4")
label1.pack(side=RIGHT, padx=20, pady=20)

# Configuração do estilo da Label com informações
info_frame = Frame(raiz, bg="#F4F4F4")
info_frame.pack(side=LEFT, padx=20, pady=20)

label2 = tkinter.Label(info_frame, text="Nome: Rāmānujan\nSobrenome: Srinivāsa", font=("Helvetica", 14), bg="#F4F4F4")
label2.pack(pady=(20,0))

animation()

raiz.title("Informações de Rāmānujan")
raiz.mainloop()

