# Problema Prático 5.10
# Escreva uma função juros() que aceite como entrada uma taxa de juros de ponto flutuante (por exemplo, 0,06, que corresponde a 6% de taxa de juros). Sua função deverá calcular e retornar quanto tempo (em anos) será necessário para que um investimento duplique seu valor. Nota: O número de anos necessário para que um investimento duplique não depende do valor do investimento inicial.
# >>> juros(0.07)
# 11

def juros(taxaDeJurosAnual):
    dinheiro = 1
    multiplicador = 1 + taxaDeJurosAnual
    anos = 0
    while dinheiro < 2:
        dinheiro *= multiplicador
        anos+=1
    return anos
