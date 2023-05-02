# Defina, diretamente no shell interativo, a função média(), que aceita dois números como entrada e retorna a média dos números.

# Feito no Shell

# Implemente a função perímetro(), que aceita, como entrada, o raio de um círculo (um número não negativo) e retorna o perímetro do círculo.
# Você deverá escrever sua implementação em um módulo chamado perímetro.py

# Feito no Shell

# Escreva a função negativos(), que aceita uma lista como entrada e exibe, um por linha, os valores negativos na lista. A função não deverá retornar nada.
def negativos(lst):
    'Aceita uma lista como entrada. Exibe, um por linha, os valores negativos na lista.'
    if not isinstance(lst, list):
        print('Somente listas serão aceitas')
        return
    for item in lst:
        if not isinstance(item, int):
            print('Somente listas de números inteiros serão aceitas')
            return
    for item in lst:
        if(item < 0):
            print(item)

# Acrescente a docstring retorna a média de x e y à função média() e
# a docstring exibe os números negativos contidos na lista lst à função negativos() dos Problemas Práticos 3.8 e 3.10.
# Verifique seu trabalho usando a ferramenta de documentação help().

# Já foi feito.

