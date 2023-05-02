import tkinter
raiz = tkinter.Tk()
tituloLabel = tkinter.Label(master=raiz,
                            font=('Helvetica', 16, 'bold italic'),
                            foreground='white',
                            background='black',
                            padx=200,
                            pady=150,
                            text='Disney+')
tituloLabel.pack(side=tkinter.LEFT)

disneyPlusFoto = tkinter.PhotoImage(file='disneyplus.gif')
disneyPlusLabel = tkinter.Label(master=raiz,
                                image=disneyPlusFoto,
                                relief=tkinter.RIDGE,
                                width=400,
                                height=300,
                                borderwidth=3)
disneyPlusLabel.pack(side=tkinter.RIGHT)

raiz.mainloop()
