# 6.11 Implemente a função criptFácil(), que aceite uma string como entrada e
# exiba sua criptografia definida da seguinte forma.
# Cada caractere em uma posição ímpar i no alfabeto será criptografado com o
# caractere na posição i + 1, e cada caractere em uma posição par i será criptografado com o
# caractere na posição i – 1. Em outras palavras 'a' é criptografado com 'b', 'b' com 'a', 'c'
# com 'd', 'd' com 'c' e assim por diante.
# Caracteres minúsculos deverão permanecer minúsculos, e caracteres maiúsculos deverão permanecer assim.
import random


def criptFacil(palavra):
    'Criptografa palavra'
    criptografado = ''
    for letra in palavra:
        if ord(letra) % 2 == 0:
            criptografado += chr(ord(letra) - 1)
        else:
            criptografado += chr(ord(letra) + 1)
    return criptografado

# 6.16 Usando um padrão de laço contador, construa conjuntos mult3,
# mult5 e mult7 de múltiplos não negativos de 3, 5 e 7,
# respectivamente, menores que 100. Depois, usando esses três conjuntos,
# escreva expressões de conjunto que retornam:
def exercicio16():
    mult3, mult5, mult7 = set(), set(), set()
    for i in range(100):
        if i % 3 == 0:
            mult3.add(i)
        if i % 5 == 0:
            mult5.add(i)
        if i % 7 == 0:
            mult7.add(i)
    print(mult3)
    print(mult5)
    print(mult7)
    item = input('Escolha um item:\n')
    if item == 'a':
        print('(a)Múltiplos de 35.\n')
        mult35 = mult5 & mult7
        print(mult35)
    elif item == 'b':
        print('(b)Múltiplos de 105.\n')
        mult35 = mult5 & mult7
        mult105 = set()
        for numero in mult35:
            mult105.add(numero * 3)
        print(mult105)
    elif item == 'c':
        print('(c)Múltiplos de 3 ou 7.\n')
        mult3ou7 = mult3 | mult7
        print(mult3ou7)
    elif item == 'd':
        print('(d)Múltiplos de 3 ou 7, mas não de ambos.\n')
        mult3ou7ExcetoAmbos = mult3 ^ mult7
        print(mult3ou7ExcetoAmbos)
    elif item == 'e':
        print('(e)Múltiplos de 7 que não sejam múltiplos de 3.\n')
        mult7QueNaoE3 = mult7 - mult3
        print(mult7QueNaoE3)

def hexaASCII():
    listaAlfabeto = []
    for i in range(ord('a'), (ord('z') + 1)):
        listaAlfabeto.append(i)
    for numero in listaAlfabeto:
        print("{}:{} ".format(chr(numero), hex(numero)[2:4]),end=' ')

def moeda():
    PROBABILIDADE_CARA_COROA = 0.5
    lance = random.uniform(0,1)
    if lance > PROBABILIDADE_CARA_COROA:
        return 'Cara'
    else:
        return 'Coroa'

# Inglês: My name is Ada
# Árabe: اسمي ادا
# Japonês: 私の名前はエイダです
# Sérvio: Моје име је Ада