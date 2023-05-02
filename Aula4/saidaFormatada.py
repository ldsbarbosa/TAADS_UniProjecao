# Problema Prático 4.3
print("Problema Prático 4.3")
# Escreva uma instrução que exibe os valores das variáveis último,
# primeiro e meio em uma linha, separadas por um caractere de tabulação horizontal.
# (A sequência de escape Python para o caractere de tabulação horizontal é \t.)
# Se as variáveis são atribuídas desta forma:
ultimo = 'Smith'
primeiro = 'John'
meio = 'Paul'
# a saída deverá ser: Smith   John   Paul
print(primeiro, ultimo, meio, sep='\t')

print("\n###\n###\n")
# Problema Prático 4.4
print("Problema Prático 4.4")
# Escreva a função par() que toma um inteiro positivo n
# como entrada e exibe na tela todos os números entre 2 (inclusive)
# e n, que sejam divisíveis por 2 ou por 3, usando este formato de saída:

def par(numero):
    'Recebe um numero e imprime os números pares até ele'
    numeroInicial = 1
    while numeroInicial <= numero:
        if numeroInicial % 2 == 0:
            print(numeroInicial, end=", ")
        numeroInicial+=1

par(17)

print("\n###\n###\n")
# Problema Prático 4.5
print("Problema Prático 4.5")
# Suponha que as variáveis primeiro, último, rua, número, cidade,
# estado, codPostal já tenham sido atribuídas.
# Escreva uma instrução print que crie uma etiqueta de correspondência:
primeiro = 'John'
ultimo = 'Doe'
rua = 'Main Street'
numero = 123
cidade = 'AnyCity'
estado = 'AS'
codPostal = '09876'
print("{0} {1}\n{2} {3}\n{4}, {5} {6}".format(primeiro,ultimo,numero,rua,cidade,estado,codPostal))

print("\n###\n###\n")
# Problema Prático 4.6
print("Problema Prático 4.6")
# Implemente a função rol(), que recebe uma lista contendo informações de estudantes e exibe um rol,
# como vemos a seguir. As informações do estudante, consistindo em seu sobrenome, nome, nível e nota média,
# serão armazenadas nessa ordem em uma lista. Portanto, a lista de entrada é uma lista de listas.
# Cuide para que o rol exibido tenha 10 espaços para cada valor de string e
# 8 para a nota, incluindo 2 espaços para a parte decimal.
estudantes = []
estudantes.append(['DeMoines', 'Jim', 'Pleno', 3.45])
estudantes.append(['Pierre', 'Sophie', 'Pleno', 4.0])
estudantes.append(['Columbus', 'Maria', 'Sênior', 2.5])
estudantes.append(['Phoenix', 'River', 'Júnior', 2.45])
estudantes.append(['Olympis', 'Edgar', 'Júnior', 3.99])
def rol(lista):
    'Imprime, em formato de tabela, os nomes, as classes e a nota média'
    ultimo = 'Último'
    primeiro = 'Primeiro'
    classe = 'Classe'
    notaMedia = 'Nota Média'
    print("{0:10} {1:10} {2:10} {3:10}".format(ultimo,primeiro,classe,notaMedia))
    for coluna in lista:
        ultimo, primeiro, classe, notaMedia = coluna[0], coluna[1], coluna[2], coluna[3]
        print("{0:10} {1:10} {2:10} {3:6.2f}".format(ultimo,primeiro,classe,notaMedia))
rol(estudantes)
