def abreviacao(diaDaSemana):
    diasDaSemana = ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado']
    if diaDaSemana in diasDaSemana:
        return diaDaSemana[0:3]
    else:
        print("Insira um dia da semana")
        return