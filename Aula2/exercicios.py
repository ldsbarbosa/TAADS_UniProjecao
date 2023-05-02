import math, random as rd
## Exercicio 12
print("##  Exercicio 12 ##\n")
print("##  Enunciado - Escreva expressões Python correspondentes a estas instruções:##\n")
# (a)
print("A soma dos sete primeiros inteiros positivos")
print(1 + 2 + 3 + 4 + 5 + 6 + 7)
print("\n")
# (b)
print("A idade média de Sara (idade 65), Fátima (idade 56) e Mark (idade 45)")
print(sum([65, 56, 45])/len([65, 56, 45]))
print("\n")
# (c)
print("2 à 20-ª potência")
print(2**20)
print("\n")
# (d)
print("O número de vezes que 61 cabe em 4356")
print(4356 // 61)
print("\n")
# (e)
print("O resto de quando 4365 é dividido por 61")
print(4356 % 61)
print("\n\n")
## Exercicio 13
print("##  Exercicio 13 ##\n")
s1 = '-'
s2 = '+'
print("##  Enunciado - Escreva expressões de string envolvendo s1 e s2 e os operadores de string + e * que são avaliados como:##\n")
# (a) e (b)
print('-+')
print(s1 + s2)
print("\n")
# (c)
print('+––')
print(s2 + (s1 * 2))
print("\n")
# (d)
print("+––+––")
print(2 * (s2 + s1 * 2))
print("\n")
# (e)
print("+––+––+––+––+––+––+––+––+––+––+")
print((10 * (s2 + s1 * 2)) + s2)
print("\n")
# (f)
print("+–+++––+–+++––+–+++––+–+++––+–+++––")
print(5 * (s2 + s1 + s2 * 3 + s1 * 2))
print("\n\n")

## Exercicio 14
print("##  Exercicio 14 ##\n")

s = 'abcdefghijklmnopqrstuvwxyz'
print("##  Enunciado - Escreva expressões usando a string s e o operador de indexação que é avaliado como 'a', 'c', 'z', 'y' e 'q'.##\n")
print(s[0])
print(s[2])
print(s[len(s)-1])
print(s[len(s)-2])
print(s[len(s)-10])

print("\n\n")

## Exercicio 15
print("##  Exercicio 15 ##\n")

s = 'goodbye'
print("##  Enunciado - Escreva uma expressão Booleana que verifica se:##\n")
# (a)
print("O primeiro caractere da string s é 'g'")
print(s[0] == 'g')
print("\n")
# (b)
print("O sétimo caractere de s é g")
print(s[6] == 'g')
print("\n")
# (c)
print("Os dois primeiros caracteres de s são g e a")
print(s[0] == 'g' and s[1] == 'a')
print("\n")
# (d)
print("O penúltimo caractere de s é x")
print(s[5] == 'x')
print("\n")
# (e)
print("O caractere do meio de s é d")
print(s[3] == 'd')
print("\n")
# (f)
print("O primeiro e último caracteres da string s são iguais")
print(s[0] == s[6])
print("\n")
# (g)
print("Os 4 últimos caracteres da string s correspondem à string 'tion'")
print(s[3:7] == 'tion')

print("\n\n")

## Exercicio 16
print("##  Exercicio 16 ##\n")

print("##  Escreva as instruções de atribuição Python correspondentes a:##\n")
# (a)
print("Atribuir 6 à variável a e 7 à variável b.")
a = 6
b = 7
print("a: " + str(a) + " b:" + str(b))
print("\n")
# (b)
print("Atribuir à variável c a média das variáveis a e b.")
c = sum([a, b])/2
print("\n")
# (c)
print("Atribuir à variável estoque a lista contendo as strings 'papel', 'grampos' e 'lápis'.")
estoque = ['papel', 'grampos', 'lápis']
print(estoque)
print("\n")
# (d)
print("Atribuir às variáveis primeiro, meio e último as strings 'John', 'Fitzgerald' e 'Kennedy'.")
primeiro = "John"
meio = "Fitzgerald"
último = "Kennedy"
print("primeiro:" + primeiro + "  meio:" + meio + "  último:" + último)
print("\n")
# (e)
print("Atribuir à variável nomecompleto a concatenação das variáveis de string primeiro, meio e último.")
nomecompleto = primeiro + " " + meio + " " + último
print("Nome completo: "+nomecompleto)
print("\n")

print("\n\n")

## Exercicio 17
print("##  Exercicio 17 ##\n")

print("## Escreva expressões Booleanas correspondentes às instruções lógicas a seguir e avalie as expressões: ##\n")
# (a)
print("A soma de 16 e –9 é menor que 10")
print(16 + (-9) < 10)
print("\n")
# (b)
print("O comprimento da lista inventário é mais de cinco vezes o comprimento da string nomecompleto")
# Como não há inventário, usei estoque
print(len(estoque) > len(nomecompleto) * 5)
print("\n")
# (c)
print("c não é maior que 24")
print(c < 24)
print("\n")
# (d)
print("6,75 está entre os valores dos inteiros a e b")
print(a < 6.75 < b)
print("\n")
# (e)
print("O comprimento da string meio é maior que o comprimento da string primeiro e menor que o comprimento da string último")
print(len(último) > len(meio) > len(primeiro))
print("\n")
# (f)
print("Ou a lista estoque está vazia ou tem mais de 10 objetos nela")
print(len(estoque) == 0 ^ len(estoque) > 10) #Ou ... ou é ou exclusivo, ou XOR. Link: https://www.scaler.com/topics/xor-in-python/
print("\n")

print("\n\n")

## Exercicio 18
print("##  Exercicio 18 ##\n")

print("## Escreva instruções Python correspondentes ao seguinte: ##\n")
# (a)
print("Atribua à variável flores uma lista contendo as strings 'rosa', 'buganvília', 'iúca', 'margarida', 'dália' e 'lírio dos vales'.")
flores = ['rosa', 'buganvília', 'iúca', 'margarida', 'dália' , 'lírio dos vales']
print(flores)
print("\n")
# (b)
print("Escreva uma expressão Booleana que é avaliada como True se a string 'batata' estiver na lista flores e avalie a expressão.")
print(flores.count('batata') != 0)
print("\n")
# (c)
print("Atribua à lista espinhosas a sublista da lista flores consistindo nos três primeiros objetos na lista.")
espinhosas = flores[0:3]
print(espinhosas)
print("\n")
# (d)
print("Atribua à lista venenosas a sublista da lista flores consistindo apenas no último objeto da lista flores.")
venenosas = flores[5:6]
print(venenosas)
print("\n")
# (e)
print("Atribua à lista perigosas a concatenação das listas espinhosas e venenosas.")
perigosas = espinhosas + venenosas
perigosas.sort()
print(perigosas)
print("\n")

print("\n\n")

## Exercicio 19
print("##  Exercicio 19 ##\n")

print("## Um alvo de dardos de raio 10 e a parede em que está pendurado são representados usando o sistema de coordenadas bidimensionais,\n" +
 "com o centro do alvo na coordenada (0,0). As variáveis x e y armazenam as coordenadas x e y de um lançamento de dardo.\n" +
 " Escreva uma expressão usando as variáveis x e y que avalia como True se o dardo atingir o (estiver dentro do) alvo,\n" +
 "e avalie a expressão para estas coordenadas do dardo: ##\n")
# (a)
print("(0, 0)")
x = 0
y = 0
diagonal = math.sqrt(x**2 + y**2)
print("Atingiu? "+str(diagonal < 10))
print("\n")
# (b)
print("(10, 10)")
x = 10
y = 10
diagonal = math.sqrt(x**2 + y**2)
print("Atingiu? "+str(diagonal < 10))
print("\n")
# (c)
print("(6, -6)")
x = 6
y = -6
diagonal = math.sqrt(x**2 + y**2)
print("Atingiu? "+str(diagonal < 10))
print("\n")
# (d)
print("(-7, 8)")
x = -7
y = 8
diagonal = math.sqrt(x**2 + y**2)
print("Atingiu? "+str(diagonal < 10))
print("\n")

print("\n\n")

## Exercicio 20
print("##  Exercicio 20 ##\n")

print("## Uma escada encostada diretamente contra uma parede cairá a menos que colocada em um certo ângulo menor que 90 graus.\n"+
" Dadas as variáveis comprimento e ângulo armazenando o comprimento da escada e o ângulo que ela forma com o solo enquanto encostada na parede,\n"+
" escreva uma expressão Python envolvendo comprimento e ângulo,\n"+
" que calcule a altura alcançada pela escada. Avalie a expressão para estes valores de comprimento e ângulo: ##\n")
# (a)
print("16 pés e 75 graus") # Aproximadamente, 5 metros
comprimento = 16
angulo = 75
altura = math.sin( (75*math.pi) / 180) * comprimento
print("Altura: "+str(round(altura,4)))
print("\n")
# (b)
print("20 pés e 0 graus") # Aproximadamente, 6 metros
comprimento = 20
angulo = 0
altura = math.sin((75*math.pi)/180) * comprimento
print("Altura: "+str(round(altura,4)))
print("\n")
# (c)
print("24 pés e 45 graus") # Aproximadamente, 7 metros
comprimento = 24
angulo = 45
altura = math.sin((75*math.pi)/180) * comprimento
print("Altura: "+str(round(altura,4)))
print("\n")
# (d)
print("24 pés e 80 graus") # Aproximadamente, 7 metros
comprimento = 24
angulo = 80
altura = math.sin((75*math.pi)/180) * comprimento
print("Altura: "+str(round(altura,4)))
print("\n")

print("\n\n")

## Exercicio 21
print("##  Exercicio 21 ##\n")

print("## Escreva uma expressão envolvendo uma string de três letras s que avalia como uma string cujos caracteres são os caracteres de s em ordem contrária.\n" +
" Se s for 'top', a expressão deverá ser avaliada como 'pot'. ##\n")
s = 'top'
print('s: '+s)
print('s inverso: '+s[::-1])
print("\n\n")

## Exercicio 22
print("##  Exercicio 22 ##\n")

print("## Escreva uma expressão envolvendo a string s contendo o último e o primeiro nome de uma pessoa —\n" +
" separados por um espaço em branco — que seja avaliada para as iniciais da pessoa. Se a string tivesse meu primeiro e último nome, a expressão seria avaliada como 'LP'.. ##\n")
s = 'Lewis Pearson'
primeiraInicial = s[0]
segundaInicial = s[s.index(' ')+1]
print('s: '+s)
print('s com as iniciais: '+primeiraInicial+segundaInicial)

print("\n\n")

## Exercicio 23
print("##  Exercicio 23 ##\n")

print("## O intervalo de uma lista de números é a maior diferença entre dois números quaisquer na lista.\n" +
" Escreva uma expressão em Python que calcule o intervalo de uma lista de números lst.\n" +
" Se a lista lst for, digamos, [3, 7, -2, 12], a expressão deverá ser avaliada como 14 (a diferença entre 12 e –2). ##\n")
lst = [3, 7, -2, 12]
intervalo = max(lst) - (min(lst))
print('Lista: '+str(lst))
print('Intervalo: '+str(intervalo))

print("\n\n")

## Exercicio 24
print("##  Exercicio 24 ##\n")

print("## Escreva a expressão ou instrução Python relevante, envolvendo uma lista de números lst e usando operadores e métodos de lista para estas especificações.: ##\n")
lst = [rd.randint(1,10),rd.randint(1,10),rd.randint(1,10),rd.randint(1,10),rd.randint(1,10),rd.randint(1,10)]
print("Lista: " + str(lst))
# (a)
print("Uma expressão que é avaliada como o índice do elemento do meio de lst")
indiceDoElementoDoMeio = str( (len(lst)-1) - ( (len(lst) - 1) // 2) )
print("Índice do elemento do meio de lst: " + indiceDoElementoDoMeio )
print("\n")
# (b)
print("Uma expressão que é avaliada como o elemento do meio de lst")
elementoDoMeio = str( lst[ (len(lst)-1) - ( (len(lst) - 1) // 2) ] )
print("Elemento do meio de lst: " + elementoDoMeio )
print("\n")
# (c)
print("Uma instrução que classifica a lista lst em ordem decrescente")
lst.sort(reverse = True)
print("lst em ordem decrescente:")
print( lst )
print("\n")
# (d)
print("Uma instrução que remove o primeiro número da lista lst e o coloca no final")
print("Antes: " + str(lst) )
elementoRetirado = lst.pop(0)
lst.append(elementoRetirado)
print("Depois: " + str(lst) )
print("\n")

print("\n\n")

## Exercicio 25
print("##  Exercicio 25 ##\n")

print("## Acrescente um par de parênteses a cada expressão de modo que ela seja avaliada como True: ##\n")
# (a)
print("0 == 1 == 2")
print(0 == (1 == 2))
print("\n")
# (b)
print("2 + 3 == 4 + 5 == 7")
print(2 + (3 == 4) + 5 == 7)
print("\n")
# (c)
print("1 < -1 == 3 > 4")
print( (1 < -1) == (3 > 4) )
print("\n")

print("\n\n")

## Exercicio 26
print("##  Exercicio 26 ##\n")
# Exercicio que usa a biblioteca turtle
print("\n\n")

## Exercicio 27
print("##  Exercicio 27 ##\n")
# Exercicio que usa a biblioteca turtle
print("\n\n")

## Exercicio 28
print("##  Exercicio 28 ##\n")
# Exercicio que usa a biblioteca turtle
print("\n\n")

## Exercicio 29
print("##  Exercicio 29 ##\n")
# Exercicio que usa a biblioteca turtle
print("\n\n")

## Exercicio 30
print("##  Exercicio 30 ##\n")
# Exercicio que usa a biblioteca turtle
print("\n\n")

## Exercicio 31
print("##  Exercicio 31 ##\n")
# Exercicio que usa a biblioteca turtle
print("\n\n")

## Exercicio 32
print("##  Exercicio 32 ##\n")
# Exercicio que usa a biblioteca turtle
print("\n\n")

## Exercicio 33
print("##  Exercicio 33 ##\n")
# Exercicio que usa a biblioteca turtle
print("\n\n")

## Exercicio 34
print("##  Exercicio 34 ##\n")
# Exercicio que usa a biblioteca turtle
print("\n\n")

## Exercicio 35
print("##  Exercicio 35 ##\n")
# Exercicio que usa a biblioteca turtle
print("\n\n")

## Exercicio 36
print("##  Exercicio 36 ##\n")
# Exercicio que usa a biblioteca turtle
print("\n\n")