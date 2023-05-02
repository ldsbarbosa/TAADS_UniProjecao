from tkinter import Tk, Label, PhotoImage
raiz = Tk()# a janela

# transforma GIF em formato que tkinter pode exibir
netflixFoto= PhotoImage(file='netflix.gif')
elemento = Label(master=raiz,
    image=netflixFoto,
    width=300,# largura do label, em pixels
    height=180)# altura do label, em pixels
elemento.pack()

raiz.mainloop()