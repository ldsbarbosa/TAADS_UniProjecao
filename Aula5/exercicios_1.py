# 12
def teste(numero):
    if numero < 0:
        print('Negativo')
    elif numero == 0:
        print('Zero')
    elif numero > 0:
        print('Positivo')

# 13
    # 14 - Laço for: Padrão de Iteração
    # 15 - Laço for: Padrão de Iteração
    # 16 - Laço for: Padrão de Iteração
    # 17 - Laço for: Padrão Contador
    # 18 - Laço for: Padrão de Iteração
    # 19 - Laço for: Padrão de Iteração
    # 20 - Laço for: Padrão Acumulador
    # 21 - Laço for: Padrão de Iteração
    # 22 - Laço for: Padrão de Iteração

# 14
def mult3(lst):
    for num in lst:
        if num % 3 == 0:
            print(num, end=", ")

#15
def vogais(palavra):
    vogais = 'aeiouAEIOU'
    for i in range(len(palavra)):
        if palavra[i] in vogais:
            print(i,end=', ')

# 16
def indices(palavra, letraDesejada):
    indicesDaPalDesejada = []
    for i in range(len(palavra)):
        if palavra[i] == letraDesejada:
            indicesDaPalDesejada.append(i)
    return indicesDaPalDesejada

# 17
def dobros(lst):
    for i in range(1,len(lst)):
        if lst[i] == lst[i-1]*2:
            print(lst[i])

#18
def quatro_letras(lst):
    palavrasCom4Letras = []
    for palavra in lst:
        if len(palavra) == 4:
            palavrasCom4Letras.append(palavra)
    return palavrasCom4Letras

#19
def emAmbas(lst, lst2):
    for item in lst:
        for item2 in lst2:
            if item == item2:
                return True
    return False

#20
def intersecao(lst, lst2):
    lstInter = []
    for item in lst:
        for item2 in lst2:
            if item == item2:
                lstInter.append(item)
    return lstInter

#21
def par(lst1, lst2, inteiroN):
    for item in lst1:
        for item2 in lst2:
            if item + item2 == inteiroN:
                print("{} {}".format(item, item2))

#22
def parSoma(lst, inteiroN):
    for i in range(len(lst) // 2):
        for j in range(len(lst)):
            if lst[i] + lst[j] == inteiroN:
                print("{} {}".format(i, j))
