# Problema Prático 5.2
# Escreva uma função chamada potências() que apanhe um inteiro positivo n como entrada e exiba, na tela, todas as potências de 2 desde 21 até 2n.
# >>> potências(6)
# 2 4 8 16 32 64
def potencias(numero):
    for i in range(1, numero+1):
        print(2**i, end=' ')

# Escreva a função aritmética(), que aceita uma lista de inteiros como entrada e retorna True se eles formarem uma sequência aritmética. (Uma sequência de inteiros é uma sequência aritmética se a diferença entre os itens consecutivos da lista for sempre a mesma.)
# >>> aritmética([3, 6, 9, 12, 15])
# True
# >>> aritmética([3, 6, 9, 11, 14])
# False
# >>> aritmética([3])
# True
def aritmetica(inteiros):
    if len(inteiros) < 2:
        return True
    diferenca = inteiros[0] - inteiros[1]
    for i in range(0, len(inteiros)-1):
        if inteiros[i] - inteiros[i+1] != diferenca:
            return False
    return True

# Problema Prático 5.4
# Implemente a função fatorial(), que toma como entrada um inteiro não negativo e retorna seu fatorial. O fatorial de um inteiro não negativo n, indicado por n!, é definido desta maneira:
# Logo, 0! = 1,3! = 6 e 5! = 120.
# >>> fatorial(0)
# 1
# >>> fatorial(3)
# 6
# >>> fatorial(5)
# 120
def fatorial(numero):
    fatorial = 1
    for i in range(1,numero+1):
        fatorial = fatorial * i
    return fatorial

# Problema Prático 5.5
# Um acrônimo é uma palavra formada tomando-se as primeiras letras das palavras em uma frase e depois criando uma palavra para elas. Por exemplo, RAM é um acrônimo para a memória de acesso aleatório (random access memory). Escreva uma função acrônimo() que aceite uma frase (ou seja, uma string) como entrada e depois retorne o acrônimo para essa frase. Nota: O acrônimo deverá estar em letras maiúsculas, mesmo que as palavras na frase não sejam iniciadas por maiúsculas.
# >>> acrônimo('Random access memory')
# 'RAM'
# >>> acrônimo('central processing unit')
# 'CPU'
# Se acumularmos objetos em uma lista, o acumulador deverá ser uma lista. Qual é a identidade para a concatenação de lista? É a lista vazia [].

def acronimo(palavra):
    palavraComIniciais = palavra[0].upper()
    for i in range(len(palavra)):
        if palavra[i] == ' ':
            palavraComIniciais += palavra[i+1].upper()
    return palavraComIniciais

# Problema Prático 5.6
# Escreva a função divisores(), que aceita um inteiro positivo n como entrada e retorna a lista de todos os divisores positivos de n.
# >>> divisores(1)
# [1]
# >>> divisores(6)
# [1, 2, 3, 6]
# >>> divisores(11)
# [1, 11]

def divisores(numero):
    divisores = []
    for i in range(1,numero+1):
        if numero % i == 0:
            divisores.append(i)
    return divisores

# Problema Prático 5.7
# Escreva uma função xmult() que aceite duas listas de inteiros como entrada e retorne uma lista contendo todos os produtos de inteiros da primeira lista com os inteiros da segunda lista.
# >>> xmult([2], [1, 5])
# [2, 10]
# >>> xmult([2, 3], [1, 5])
# [2, 10, 3, 15]
# >>> xmult([3, 4, 1], [2, 0])
# [6, 0, 8, 0, 2, 0]

def xmult(lista1, lista2):
    lista3 = []
    for numero1 in lista1:
        for numero2 in lista2:
            lista3.append(numero1*numero2)
    return lista3

# Problema Prático 5.8
# Uma forma de classificar uma lista de n números diferentes em ordem crescente é executar n –1 passadas sobre os números na lista. Cada passada compara todos os números adjacentes na lista e os inverte, se estiverem fora da ordem. Ao final da primeira passada, o maior item estará no final da lista (no índice n – 1). Portanto, a segunda passada pode parar antes de alcançar o último elemento, pois ele já está na posição correta; a segunda passada colocará o segundo maior item na penúltima posição. Em geral, a passada i comparará os pares nos índices 0 e 1, 1 e 2, 2 e 3, …, e i – 1 e i; ao final da passada, o i-ésimo maior item estará no índice n – i. Portanto, após a passada n – 1, a lista estará em ordem crescente.
# Escreva uma função bubbleSort() que aceite uma lista de números como entrada e classifique a lista usando essa técnica.
# >>> lst = [3, 1, 7, 4, 9, 2, 5]
# >>> bubblesort(lst)
# >>> lst
# [1, 2, 3, 4, 5, 7, 9]

def bubbleSort(lst):
    for j in range(round(len(lst)/2)):
        for i in range(len(lst) - 1):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
    return lst