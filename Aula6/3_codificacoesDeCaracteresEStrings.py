# Problema Prático 6.7
# Escreva uma função codifica(), que aceite uma string como entrada e exiba o código ASCII
# — em notação decimal, hexa e binária — de cada caractere nela contida.
# >>> codifica('dad')
# Car  Decimal  Hexa  Binário
#  d       100   64  1100100
#  a        97   61  1100001
#  d       100   64  1100100
# A função chr() é o inverso da função ord().
# Ela apanha um código numérico e retorna o caractere correspondente a ele.
# >>> chr(97)
# 'a'

def codifica(cadeiaDeCaracteres):
    listaCadeiaDeCaracteres = []
    listaCadeiaDeCaracteresDec = []
    listaCadeiaDeCaracteresHex = []
    listaCadeiaDeCaracteresBin = []
    for char in cadeiaDeCaracteres:
        listaCadeiaDeCaracteres.append(char)
        listaCadeiaDeCaracteresDec.append(ord(char))
        listaCadeiaDeCaracteresHex.append(hex(ord(char)))
        listaCadeiaDeCaracteresBin.append(bin(ord(char)))
    
    print('{:8}\t{:8}\t{:8}\t{:8}'.format('Car','Decimal','Hexa','Binário'))
    for i in range(len(listaCadeiaDeCaracteres)):
        print('{:8}\t{:8}\t{:8}\t{:8}'.format(listaCadeiaDeCaracteres[i],
                                              listaCadeiaDeCaracteresDec[i],
                                              listaCadeiaDeCaracteresHex[i],
                                              listaCadeiaDeCaracteresBin[i]
                                              ))

# Problema Prático 6.8
# Escreva a função char(início, fim), que exiba os caracteres
# correspondentes aos códigos decimais i para todos os valores de i desde início até fim, inclusive.
# >>> char(62, 67)
# 62 : >
# 63 : ?
# 64 : @
# 65 : A
# 66 : B
# 67 : C
def char(inicio, fim):
    for i in range(inicio, fim+1):
        print("{} : {}".format(i,chr(i)))
