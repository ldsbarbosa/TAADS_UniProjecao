from tkinter import Tk, Label, PhotoImage, BOTTOM, LEFT, RIGHT, RIDGE
raiz = Tk()  # a janela

tituloLabel = Label(raiz,
              font=('Helvetica', 16, 'bold italic'),
              foreground='white', # cor da letra
              background='black', # cor do fundo
              padx=25,  # expande label 25 pixels para esquerda e direita
              pady=10,  # amplia label 10 pixels acima e abaixo
              text='Grandes empresas de tecnologia na área de Streaming.')

tituloLabel.pack(side=BOTTOM)# empurra label para baixo

# transforma GIF em formato que tkinter pode exibir
netflixFoto = PhotoImage(file='netflix.gif')
netflixLabel = Label(master=raiz,
                 image=netflixFoto,
                 relief=RIDGE,
                 borderwidth=3)
netflixLabel.pack(side=LEFT)

amPrimeFoto = PhotoImage(file='amazon-prime.gif')
amPrimeLabel = Label(master=raiz,
                     image=amPrimeFoto)
amPrimeLabel.pack(side=RIGHT)
raiz.mainloop()
