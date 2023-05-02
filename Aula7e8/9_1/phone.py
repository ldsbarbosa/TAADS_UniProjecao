from tkinter import Tk, Label, RAISED

raiz = Tk()

labels = [['1', '2', '3'],
          ['4', '5', '6'],
          ['7', '8', '9'],
          ['*', '0', '#']]

for r in range(len(labels)):
    for c in range(len(labels[r])):
        label = Label(raiz,
                      relief=RAISED,
                      padx=10,
                      text=labels[r][c])
        label.grid(row=r, column=c)

raiz.mainloop()
