# netflix.py
# netflixAmPrime.py
# prob pratico 1 ->  disneyplus.py
# phone.py
# prob pratico 2
import calendar, tkinter as tk

def cal(ano, mes):
    diasDaSemana = {
        "Dom":[],
        "Seg":[],
        "Ter":[],
        "Qua":[],
        "Qui":[],
        "Sex":[],
        "Sab":[]
    }
    diasDaSemanaLista = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sab", "Dom"]
    primeiroDia, qtdDias = calendar.monthrange(ano, mes)
    diaDaSemanaInicial = diasDaSemanaLista[primeiroDia]
    
    for dia in range(1, qtdDias+1):
        diaDaSemana = diasDaSemanaLista[(diasDaSemanaLista.index(diaDaSemanaInicial) + dia - 1) % 7]
        diasDaSemana[diaDaSemana].append(dia)
        
    return diasDaSemana

root = tk.Tk()

ano = 2023
mes = 4

diasDaSemana = cal(ano, mes)

# Nome do mês e ano
mes_ano = tk.Label(root, text=calendar.month_name[mes] + " " + str(ano), font=("Arial", 18, "bold"))
mes_ano.grid(row=0, column=0, columnspan=7)

# Dias da semana
dias_da_semana = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sab", "Dom"]
for i, dia in enumerate(dias_da_semana):
    label = tk.Label(root, text=dia, font=("Arial", 12, "bold"))
    label.grid(row=1, column=i, padx=5, pady=5)

# Linha horizontal separando cabeçalho e dias do mês
linha_separadora = tk.Frame(root, height=2, bd=1, relief="sunken")
linha_separadora.grid(row=2, column=0, columnspan=7, sticky="we", padx=5, pady=5)

# Criação dos labels
labels = [[None for j in range(7)] for i in range(6)]

for i in range(6):
    for j in range(7):
        label = tk.Label(root, text="", font=("Arial", 12))
        label.grid(row=i+3, column=j, padx=5, pady=5)
        labels[i][j] = label

# Preenchimento dos labels com os dias do mês
for diaDaSemana, dias in diasDaSemana.items():
    for dia in dias:
        linha = (dia - 1) // 7
        coluna = dias_da_semana.index(diaDaSemana)
        labels[linha][coluna].configure(text=str(dia))

# Borda externa
for i in range(7):
    root.grid_columnconfigure(i, weight=1)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(8, weight=1)

# Início da aplicação
root.mainloop()
