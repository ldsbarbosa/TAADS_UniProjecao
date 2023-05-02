import random
# 5.23 Escreva a função pagar(), que aceite como entrada um salário horário e o número de horas que um empregado trabalhou na última semana. A função deverá calcular e retornar o pagamento do empregado. O trabalho em hora extra deverá ser pago da seguinte forma: qualquer total de horas além de 40, porém menor ou igual a 60, deverá ser pago a 1,5 vez o salário horário normal. Qualquer total além de 60 deverá ser pago a duas vezes o salário horário normal.
def pagar(salHor, numHor):
    if numHor <= 40:
        pagamentoEmpregado = salHor * numHor
    elif 40 < numHor <= 60:
        pagamentoEmpregado = (salHor * 40) + (salHor * ((numHor-40) * 1.5))
    elif 60 < numHor:
        pagamentoEmpregado = (salHor * 40) + (salHor * (20 * 1.5)) + (salHor * ((numHor-60) * 2))
    return int(pagamentoEmpregado)

# 5.24 Escreva a função case(), que aceite uma string como entrada e retorne 'inicial maiúscula', 'inicial minúscula' ou 'desconhecido', dependendo se a string começa com uma letra maiúscula, uma letra minúscula ou algo diferente de uma letra do nosso alfabeto, respectivamente.
def case(cadeiaDeCaracteres):
    if cadeiaDeCaracteres[0].isupper():
        return 'inicial maiúscula'
    elif cadeiaDeCaracteres[0].islower():
        return 'inicial minúscula'
    else:
        return 'desconhecido'
# 5.25 Implemente a função bissexto(), que aceite um argumento de entrada — um ano — e retorne True se o ano for um ano bissexto e False caso contrário. (Um ano é ano bissexto se for divisível por 4, mas não por 100, a menos que seja divisível por 400, quando será um ano bissexto. Por exemplo, 1700, 1800 e 1900 não são anos bissextos, mas 1600 e 2000 são.)
def bissexto(ano):
    if ano % 4 and ano % 100:
        if ano % 400:
            return True
        else:
            return False
    if ano % 4:
        return True
    return False
# 5.26 Pedra, Papel, Tesoura é um jogo de dois jogadores no qual cada jogador escolhe um de três itens. Se os dois jogadores escolherem o mesmo item, o jogo fica empatado. Caso contrário, as regras que determinam o vencedor são:
def pedraPapelTesoura(escolha):
    possibilidades = ('Pedra','Papel','Tesoura')
    if escolha not in possibilidades:
        return
    escolhaMaquina = possibilidades[random.randint(0,2)]
    if  (escolha == 'Pedra' and escolhaMaquina == 'Tesoura') or (escolha == 'Tesoura' and
         escolhaMaquina == 'Papel') or (escolha == 'Papel' and escolhaMaquina == 'Pedra'):
        return 1
    elif (escolhaMaquina == 'Pedra' and escolha == 'Tesoura') or (escolhaMaquina == 'Tesoura' and
         escolha == 'Papel') or (escolhaMaquina == 'Papel' and escolha == 'Pedra'):
        return -1
    else:
        return 0

# 5.27 Escreva a função letra2número(), que aceite como entrada uma nota de letra (A, B, C, D, F, possivelmente com um – ou um +) e retorne a nota numérica correspondente. Os valores numéricos para A, B, C, D e F são 4, 3, 2, 1, 0. Um + aumenta o valor da nota numérica em 0,3 e um – a diminui em 0,3.
def letraParaNumero(letra):
    letrasPossiveis = ('A','B','C','D','F')
    if len(letra) > 1:
        if (letra[0] not in letrasPossiveis):
            return
        if letra[0] == 'A':
            numero = 4.0
        elif letra[0] == 'B':
            numero = 3.0
        elif letra[0] == 'C':
            numero = 2.0
        elif letra[0] == 'D':
            numero = 1.0
        if letra[1] == '+':
            numero = numero + 0.3
        elif letra[1] == '-':
            numero = numero - 0.3
        return numero
    else:
        if (letra not in letrasPossiveis):
            return
        if letra == 'A':
            numero = 4.0
        elif letra == 'B':
            numero = 3.0
        elif letra == 'C':
            numero = 2.0
        elif letra == 'D':
            numero = 1.0
        return numero
# 5.28 Escreva a função geométrica(), que aceite uma lista de inteiros como entrada e retorne True se os inteiros na lista formarem uma sequência geométrica. Uma sequência a0, a1, a2, a3, a4, …, an – 2, an – 1 é uma sequência geométrica se as razões a1/a0, a2/a1, a3/a2, a4/a3, …, an-1/an-2 forem todas iguais.
def geometrica(lst):
    for i in range(len(lst)-2):
        if lst[i]/lst[i+1] != lst[i+1]/lst[i+2]:
            return False
    return True
# 5.29 Escreva a função últimoprimeiro(), que aceite um argumento — uma lista de strings no formato <Sobrenome, Nome> — e retorne uma lista consistindo em duas listas:
def ultimoPrimeiro(lst):
    nomes, sobrenomes = [], []
    for item in lst:
        nomes.append(item[0:item.index(',')])
        sobrenomes.append(item[item.index(',')+1:len(item)])
    return [nomes, sobrenomes]
# 5.30 Desenvolva a função muitos(), que aceite como entrada o nome de um arquivo no diretório atual (como uma string) e gere o número de palavras de tamanho 1, 2, 3 e 4. Teste sua função no arquivo sample.txt.
def muitos(nomeDeArquivo):
    arquivo = open(nomeDeArquivo, 'r')

    tamanho_palavras = [0, 0, 0, 0]
    palavras = arquivo.read().split()

    for palavra in palavras:
        tamanho = len(palavra)
        if 1 <= tamanho <= 4:
            tamanho_palavras[tamanho-1] += 1
    arquivo.close()
    for i in range(len(tamanho_palavras)):
        print("Palavras de tamanho {}: {}".format(i+1,tamanho_palavras[i]))
# 5.31 Escreva uma função subSoma(), que aceite como entrada uma lista de números positivos e um número positivo alvo. Sua função deverá retornar True se houver três números na lista que, somados, resultem no alvo. Por exemplo, se a lista de entrada for [5, 4, 10, 20, 15, 19] e o alvo for 38, então True deve ser retornado, pois 4 + 15 + 19 = 38. Porém, se a lista de entrada for a mesma, mas o valor de alvo for 10, então o valor retornado deverá ser False, pois 10 não é a soma de três números quaisquer na lista informada.
def subSoma(lst, numeroAlvo):
    for num in lst:
        if num < 0:
            return
    if numeroAlvo < 0:
        return
    for i in range(len(lst) - 2):
        for j in range(i + 1, len(lst) - 1):
            for k in range(j + 1, len(lst)):
                if lst[i] + lst[j] + lst[k] == numeroAlvo:
                    return True
    return False
# 5.32 Implemente a função fib(), que aceite um inteiro não negativo n como entrada e retorne o n-ésimo número de Fibonacci.
def fib(nEsimo):
    fibonacci = [1,1]
    if nEsimo <= 1:
        return 1
    else:
        while len(fibonacci) <= nEsimo:
            fibonacci.append(fibonacci[len(fibonacci)-2] + fibonacci[len(fibonacci)-1])
        return fibonacci[len(fibonacci)-1]
# 5.33 Implemente uma função mistério(), que aceite como entrada um inteiro positivo n e respostas a esta pergunta: Quantas vezes n pode ser dividido ao meio (usando a divisão de inteiros) antes de alcançar 1? Esse valor deverá ser retornado.
def misterio(numero):
    contador = 0
    while numero > 1:
        numero = numero // 2
        contador+=1
    return contador
# 5.34 Escreva uma função extrato(), que aceite como entrada uma lista de números de ponto flutuante, com números positivos representando depósitos e números negativos representando retiradas de uma conta bancária. Sua função deverá retornar uma lista de dois números de ponto flutuante; o primeiro será a soma dos depósitos, e o segundo (um número negativo) será a soma das retiradas.
def extrato(lst):
    agrupamentoDepSaque = [0,0]
    for num in lst:
        if num < 0:
            agrupamentoDepSaque[0] += num
        elif num > 0:
            agrupamentoDepSaque[1] += num
    return agrupamentoDepSaque
# 5.35 Implemente a função pixels(), que aceite como entrada uma lista bidimensional de entradas de inteiros não negativos (representando os valores de pixels de uma imagem) e retorne o número de entradas que são positivas (ou seja, o número de pixels que não são escuros). Sua função deverá funcionar com listas bidimensionais de qualquer tamanho.
def pixels(lst):
    contador = 0
    for item in lst:
        for subitem in item:
            if subitem != 0:
                contador+=1
    return contador
# 5.36 Implemente a função primo(), que aceite um inteiro positivo como entrada
# e retorne True se ele for um número primo e False caso contrário.
def primo(numero):
    if numero < 0:
        return
    for i in range(2,numero):
        if numero % i == 0:
            return False
    return True
# 5.37 Escreva a função mssl() (sublista de soma máxima), que aceite como entrada uma lista de inteiros. Depois, ela calcula e retorna a soma da sublista de soma máxima da lista de entrada. A sublista de soma máxima é a sublista (pedaço) da lista de entrada cuja soma de entradas seja a maior. A sublista vazia é definida como tendo soma 0. Por exemplo, a sublista de soma máxima da lista
def sublista_soma_maxima(lst):
    if all(num < 0 for num in lst):
        return 0
    soma_maxima = soma_atual = lst[0]
    for num in lst[1:]:
        soma_atual = max(num, soma_atual + num)
        soma_maxima = max(soma_maxima, soma_atual)
    return soma_maxima

def sublista_soma_maxima2(lst):
    if all(num < 0 for num in lst):
        return []
    soma_maxima = soma_atual = lst[0]
    inicio = fim = 0
    for i, num in enumerate(lst[1:], start=1):
        if num > soma_atual + num:
            soma_atual = num
            inicio = i
        else:
            soma_atual += num
        if soma_atual > soma_maxima:
            soma_maxima = soma_atual
            fim = i
    return lst[inicio:fim+1]

# 5.38 Escreva a função collatz(), que aceite um inteiro positivo x como entrada e exibe a sequência de Collatz começando em x. Uma sequência de Collatz é obtida aplicando repetidamente essa regra ao número anterior x na sequência:
def collatz(x):
    while x != 1:
        print(x)
        if x % 2 == 0:
            x = x // 2
        else:
            x = 3 * x + 1
    print(1)

# 5.39 Escreva a função exclamação(), que aceite como entrada uma string e a retorne com esta modificação: cada vogal é substituída por quatro cópias consecutivas de si mesmo e um ponto de exclamação (!) é acrescentado no final.
def exclamacao(palavra):
    novaPalavra = ""
    for i in range(len(palavra)):
        if palavra[i] in 'aeiouAEIOU':
            novaPalavra += palavra[i]*4
        else:
            novaPalavra += palavra[i]
        if i == len(palavra) - 1:
            novaPalavra += "!"
    return novaPalavra
# 5.40 A constante π é um número irracional com valor aproximado de 3,1415928… O valor exato de π é igual a esta soma infinita:
def aproxPi(erro):
    termoDenominador = 1
    somaAtual = 4 / termoDenominador
    somaAnterior = 0
    menosOuMais = True
    while abs(somaAtual - somaAnterior) >= erro:
        termoDenominador += 2
        somaAnterior = somaAtual
        if menosOuMais:
            somaAtual -= (4 / termoDenominador)
        else:
            somaAtual += (4 / termoDenominador)
        menosOuMais = not menosOuMais
    return somaAtual
# 5.41 Um polinômio de grau n com coeficientes a0, a1, a2, a3, …, an é a função
def poli(lst,num):
    soma = 0
    for i in range(len(lst)):
        if i < 2:
            soma += lst[i] * ((num * i) ** i)
        else:
            soma += lst[i] * (num ** i)
    return soma
# 5.42 Implemente a função fatPrimo(), que aceite como entrada um inteiro positivo n e retorne uma lista contendo todos os números nos fatores primos de n. (Os fatores primos de um inteiro positivo n é a lista exclusiva de números primos cujo produto é n.)
def fatPrimo(num):
    listaDivisoresPrimos = []
    controlador = False
    for i in range(2,num):
        # Laço para verificar se i é primo
        for j in range(2, i):
            if i % j == 0:
                controlador = not controlador
        # Saída do laço caso i não seja primo
        if controlador:
            controlador = not controlador
        else:
            while num % i == 0:
                num = num // i
                listaDivisoresPrimos.append(i)
    return listaDivisoresPrimos
# 5.43 Implemente a função linhaPar(), que aceite uma lista bidimensional de inteiros e retorne True se cada linha da tabela totalizar um número par e False caso contrário (isto é, se alguma linha totalizar um número ímpar).
def linhaPar(lst):
    soma = 0
    for sublst in lst:
        for item in sublst:
            soma += item
        if soma % 2 != 0:
            return False
        soma = 0
    return True
# 5.44 Uma cifra de substituição para os dígitos 0, 1, 2, 3, …, 9 substitui cada dígito em 0, 1, 2, 3, …, 9 por outro dígito em 0, 1, 2, 3, …, 9. Ele pode ser representado como uma string de 10 dígitos, especificando como cada dígito em 0, 1, 2, 3, …, 9 é substituído. Por exemplo, a string de 10 dígitos '3941068257' especifica uma cifra de substituição em que o dígito 0 é substituído pelo dígito 3, 1 por 9, 2 por 4 e assim por diante. Para criptografar um inteiro não negativo, substitua cada um de seus dígitos pelo dígito especificado na chave de criptografia.
def cifra(chave, texto_claro):
    # Cifragem do texto claro
    texto_cifrado = ""
    for digito in texto_claro:
        texto_cifrado += chave[int(digito)]
    return texto_cifrado

# 5.45 A função médiamédia() aceita como entrada uma lista cujos itens são listas de três números. Cada lista de três números representa as três notas que determinado estudante recebeu para um curso. Por exemplo, aqui está uma lista de entrada para uma turma de quatro estudantes:
def mediaMedia(lst):
    lstMedia = []
    soma = 0
    for sublst in lst:
        for item in sublst:
            soma += item
        lstMedia.append(soma / len(sublst))
        soma = 0
    return lstMedia
# 5.46 Uma inversão em uma sequência é um par de entradas que estão fora da ordem. Por exemplo, os caracteres F e D formam uma inversão na string 'ABBFHDL', pois F aparece antes de D; o mesmo ocorre com os caracteres H e D. O número total de inversões em uma sequência (ou seja, o número de pares que estão fora da ordem) é uma medida de como a sequência está desordenada. O número total de inversões em 'ABBFHDL' é 2. Implemente a função inversões(), que aceite uma sequência (ou seja, uma string) de caracteres maiúsculos de A até Z e retorne o número de inversões na sequência.
def inversoes(seq):
    count = 0
    for i in range(len(seq)):
        for j in range(i+1, len(seq)):
            if seq[i] > seq[j]:
                count += 1
    return count

def inversoes2(string):
    if len(string) <= 1:
        return 0, string

    meio = len(string) // 2
    esquerda = string[:meio]
    direita = string[meio:]

    inv_esq, esquerda = inversoes2(esquerda)
    inv_dir, direita = inversoes2(direita)

    inv = inv_esq + inv_dir
    i = j = 0
    resultado = []
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] <= direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1
            inv += len(esquerda) - i

    resultado += esquerda[i:]
    resultado += direita[j:]

    return inv, ''.join(resultado)

# 5.47 Escreva a função d2x(), que aceite como entrada um inteiro não negativo n (na representação decimal padrão) e um inteiro x entre 2 e 9, e retorne uma string de dígitos que corresponda à representação de n na base x.
def d2x(n, x):
    if n == 0:
        return '0'
    digits = []
    while n > 0:
        remainder = n % x
        digits.append(str(remainder))
        n //= x
    return ''.join(digits[::-1])

# 5.48 Considere que lista1 e lista2 sejam duas listas de inteiros. Dizemos que lista1 é uma sublista de lista2 se os elementos em lista1 aparecerem em lista2 na mesma ordem em que aparecem em lista1, mas não necessariamente de forma consecutiva. Por exemplo, se lista1 for definida como
def sublista(lista1, lista2):
    i = 0
    for x in lista2:
        if lista1[i] == x:
            i += 1
            if i == len(lista1):
                return True
    return False

# 5.49 O método de Heron é um método dos gregos antigos usado para calcular a raiz quadrada de um número n. O método gera uma sequência de números que representa aproximações cada vez melhores para . O primeiro número na sequência é uma escolha qualquer; cada outro número na sequência é obtido a partir do número anterior ant usando a fórmula
def heron(n, erro):
    a = 1.0    
    while True:
        a_nova = (a + (n / a)) / 2
        if abs(a_nova - a) < erro:
            return a_nova
        a = a_nova
