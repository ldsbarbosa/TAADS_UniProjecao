import math
## 20 a 30
print('Exercícios')
print('\n######\n')
# Escreva laços for que usam a função range() e exibem as seguintes sequências:
print('Ex1. Escreva laços for que usam a função range() e exibem as seguintes sequências:')
# (a) 0 1
print('(a)')
for item in range(0,2):
    print(str(item), end=', ')
print("\n##")
# (b) 0
print('(b)')
for item in range(0,1):
    print(str(item), end=', ')
print("\n##")
# (c) 3 4 5 6
print('(c)')
for item in range(3,7):
    print(str(item), end=', ')
print("\n##")
# (d) 1
print('(d)')
for item in range(1,2):
    print(str(item), end=', ')
print("\n##")
# (e) 0 3
print('(e)')
for item in range(0,4,3):
    print(str(item), end=', ')
print("\n##")
# (f) 5 9 13 17 21
print('(f)')
for item in range(5,22,4):
    print(str(item), end=', ')
print("\n##")
print("\n####\n")

# Implemente um programa que solicita uma
# lista de palavras do usuário e depois exibe cada palavra na lista que não seja 'segredo'.
print('Ex2.')
lst = eval(input("Insira uma lista de palavras:\n"))
for item in lst:
    if item != 'segredo':
        print(item)
print("\n####\n")

# Implemente um programa que solicita
# uma lista de nomes de aluno do usuário e exiba aqueles nomes que começam com as letras de A até M.
print('Ex3.')
lst = eval(input("Insira uma lista de nomes:\n"))
lstIniciais = ['A','B','C','D','E','F','G','H','I','J','K','L','M']
for item in lst:
    if item[0] in lstIniciais:
        print(item)
print("\n####\n")

#  Implemente um programa que
#  solicite uma lista não vazia do usuário e exiba na tela uma mensagem mostrando o primeiro e o último elemento da lista.
print('Ex4.')
lst = eval(input("Insira uma lista de números:\nLembrete, a lista não pode ser vazia.\n"))
listaVazia = False
if lst == []:
    listaVazia = True
    while listaVazia:
        lst = eval(input("Insira novamente:\n"))
for item in lst:
    if item == lst[0]:
        print("O primeiro elemento da lista é "+str(item))
    if item == lst[len(lst)-1]:
        print("O último elemento da lista é "+str(item))
print("\n####\n")

# Implemente um programa que solicita um inteiro positivo n
# do usuário e exiba os quatro primeiros múltiplos de n:
print('Ex5.')
numero = eval(input("Insira um número inteiro\n"))
for item in range(0,4):
    print(str(numero*item))
print("\n####\n")

# Implemente um programa que solicita um inteiro n do usuário e
# imprime na tela os quadrados de todos os números de 0 até, mas não incluindo, n.
print('Ex6.')
numero = eval(input("Insira outro número inteiro\n"))
for item in range(0,numero):
    print(str(item**2))
print("\n####\n")

# Implemente um programa que solicita um inteiro positivo n e exibe na tela todos os divisores positivos de n.
# Nota: 0 não é um divisor de qualquer inteiro, e n divide por si mesmo.
print('Ex7.')
numero = eval(input("Insira outro número inteiro\n"))
for item in range(1,numero+1):
    if numero % item == 0:
        print(str(item))
print("\n####\n")

# Implemente um programa que solicita quatro números (inteiro ou ponto flutuante) do usuário. Seu programa deverá calcular a média dos
# três primeiros números e comparar a média com o quarto número. Se elas forem iguais, seu programa deverá exibir 'Igual' na tela.
print('Ex8.')
listaDeNumeros = []
for i in range(0,4):
    listaDeNumeros.append(eval(input("Insira o numero da posicao {} do vetor. Este pode ser inteiro ou ponto flutuante.\n".format(i+1))))
if (sum(listaDeNumeros) / len(listaDeNumeros)) == listaDeNumeros[len(listaDeNumeros) - 1]:
    print("Igual")
print("\n####\n")

# Implemente um programa que solicita ao usuário que entre com as coordenadas x e y (cada um entre –10 e 10)
# de um dardo e calcula se o dardo atingiu o alvo, um círculo com centro (0,0) e raio 8.
# Se tiver atingido, a string Está dentro! deverá ser exibida na tela.
print('Ex9.')
coordenadaX = eval(input("Insira a coordenadas X\n"))
coordenadaY = eval(input("Insira a coordenadas Y\n"))
raioAtingido = math.sqrt(coordenadaX**2 + coordenadaY**2)
if raioAtingido <= 8:
    print("Está dentro!")
print("\n####\n")

# Escreva um programa que solicita um inteiro positivo de quatro dígitos do usuário e exibe seus dígitos.
# Você não poderá usar as operações do tipo de dados string para realizar essa tarefa.
# Seu programa deverá simplesmente ler a entrada como um inteiro e processá-la como um inteiro,
# usando as operações aritméticas padrão (+, *, -, /, % etc.).
print('Ex10.')
numero = eval(input("Insira um número inteiro positivo maior do que 0\n"))
qtdDigitos = int(math.log10(numero))+1
digito = 0
contador = qtdDigitos - 1
for item in range(0, qtdDigitos):
    digito = numero // 10**(contador)
    digito = digito % 10
    print("Digito {}: {}".format((item+1),digito))
    contador-=1
print("Numero completo: {}".format(numero))
print("\n####\n")
