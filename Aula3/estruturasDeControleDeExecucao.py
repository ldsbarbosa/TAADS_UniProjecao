#Traduza estas instruções condicionais em instruções if do Python:
# 
# (a)Se idade é maior que 62, exiba 'Você pode obter benefícios de pensão'.
# (b)Se o nome está na lista ['Musial', 'Aaraon', 'Williams', 'Gehrig', 'Ruth'], exiba 'Um dos 5 maiores jogadores de beisebol de todos os tempos!'.
# (c)Se golpes é maior que 10 e defesas é 0, exiba 'Você está morto...'.
# (d)Se pelo menos uma das variáveis booleanas norte, sul, leste e oeste for True, exiba 'Posso escapar.'.

print("(a)")
idade = int(input('Insira a idade: '))
if idade > 62:
    print('Você pode obter benefícios de pensão')
print('\n#####\n')

print("(b)")
lista = ['Musial', 'Aaraon', 'Williams', 'Gehrig', 'Ruth']
nome = input('Insira um nome: ')
if nome in lista:
    print('Um dos 5 maiores jogadores de beisebol de todos os tempos!')
print('\n#####\n')

print("(c)")
golpes = int(input('Insira a quantidade de golpes: '))
defesas = int(input('Insira a quantidade de defesas: '))
if golpes > 10 and defesas == 0:
    print('Você está morto…')
print('\n#####\n')

print("(d)")
norte = bool(input('Norte verdadeiro? '))
sul = bool(input('Sul verdadeiro? '))
leste = bool(input('Leste verdadeiro? '))
oeste = bool(input('Oeste verdadeiro? '))
if norte == True or sul == True or leste == True or oeste == True:
    print('Posso escapar.')
print('\n#####\n')

# Traduza estas declarações em instruções if/else do Python:
# (a)Se ano é divisível por 4, exiba 'Pode ser um ano bissexto.'; caso contrário, exiba 'Definitivamente não é um ano bissexto.'
# (b)Se a lista bilhete é igual à lista loteria, exiba 'Você ganhou!'; se não, exiba 'Melhor sorte da próxima vez...'.
print("(a)")
ano = int(input('Insira um ano: '))
if ano % 4 == 0 :
    print('Pode ser um ano bissexto.')
else:
    print('Definitivamente não é um ano bissexto')
print('\n#####\n')

print("(b)")
loteria = [12, 52, 45, 35]
bilhete = [0, 0, 0, 0]
for i in range(0,4):
    bilhete[i] = int(input('Insira um numero: '))
if bilhete == loteria:
    print('Você ganhou!')
else:
    print('Melhor sorte da próxima vez...')
print('\n#####\n')

# Implemente um programa que comece pedindo ao usuário para digitar uma identificação de login (ou seja, uma string).
# O programa, então, verifica se a identificação informada pelo usuário está na lista ['joe', 'sue', ' hani', 'sophie' ] de usuários válidos.
# Dependendo do resultado, uma mensagem apropriada deverá ser impressa.
# Não importando o resultado, sua função deverá exibir 'Fim.' antes de terminar.
usuarios = ['joe', 'sue', ' hani', 'sophie' ]
login = input('Login: ')
if login in usuarios:
    print('Você entrou!')
else:
    print('Usuário desconhecido')
print("Fim.")
print('\n#####\n')

# Implemente um programa que solicite do usuário uma lista de palavras (ou seja, strings) e
# depois exiba na tela, uma por linha, todas as strings de quatro letras nessa lista.
listaDePalavras = input('Insira uma lista de palavras: ').split(',')
for palavra in listaDePalavras:
    print(palavra, end=' ')
print('\n#####\n')

# Escreva o laço for que exibirá as sequências de números a seguir, um por linha, no shell interativo do Python.
# (a)Inteiros de 0 a 9 (isto é, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9).
# (b)Inteiros de 0 a 1 (isto é, 0, 1).
print("(a)")
sequenciaDeNumeros = range(0,10)
for numero in sequenciaDeNumeros:
    print(numero,end='\t')

print("\n(b)")
sequenciaDeNumeros = range(0,2)
for numero in sequenciaDeNumeros:
    print(numero,end='\t')
print('\n#####\n')

# Escreva um laço for que exiba a seguinte sequência de números, um por linha.
# (a)Inteiros de 3 até 12, inclusive este.
# (b)Inteiros de 0 até (mas não incluindo) 9, com um passo de 2 em vez do padrão 1 (isto é, 0, 2, 4, 6, 8).
# (c)Inteiros de 0 até (mas não incluindo) 24, com um passo de 3.
# (d)Inteiros de 3 até (mas não incluindo) 12, com um passo de 5.

print("(a)")
sequenciaDeNumeros = range(3,13)
for numero in sequenciaDeNumeros:
    print(numero,end='\t')

print("\n(b)")
sequenciaDeNumeros = range(0,9,2)
for numero in sequenciaDeNumeros:
    print(numero,end='\t')

print("\n(c)")
sequenciaDeNumeros = range(0,24,3)
for numero in sequenciaDeNumeros:
    print(numero,end='\t')

print("\n(d)")
sequenciaDeNumeros = range(3,12,5)
for numero in sequenciaDeNumeros:
    print(numero,end='\t')
print('\n#####\n')

