# Problema Prático 4.7
print("Problema Prático 4.7")
# Escreva a função stringCount() que aceita duas entradas de string —
# um nome de arquivo e uma string de alvo —
# e retorna o número de ocorrências da string alvo no arquivo.
# stringCount('example.txt', 'line')
# 4
def stringCount(nomeDoArquivo, stringOcorrencia):
    'Quantas vezes a string ocorre no arquivo'
    arqEntrada = open(nomeDoArquivo, 'r')
    conteudo = arqEntrada.read()
    arqEntrada.close()
    print(str(conteudo.count(stringOcorrencia)))
    return conteudo.count(stringOcorrencia)
stringCount('example.txt','line')

print("\n###\n###\n")
# Problema Prático 4.8
print("Problema Prático 4.8")
# Escreva a função palavras() que aceita um argumento de entrada — um nome de arquivo — e retorna a lista de palavras reais (sem símbolos de pontuação !,.:;?) no arquivo.
# palavras('example.txt')
# ['The', '3', 'lines', 'in', 'this', 'file', 'end', 'with',
#  'the', 'new', 'line', 'character', 'There', 'is', 'a',
#  'blank', 'line', 'above', 'this', 'line']
def palavras(nomeDoArquivo):
    'Dividir o arquivo em palavras numa lista'
    arqEntrada = open(nomeDoArquivo, 'r')
    conteudo = arqEntrada.read()
    arqEntrada.close()
    print(str(conteudo.split()))
    return conteudo.split()
palavras('example2.txt')

print("\n###\n###\n")
# Problema Prático 4.9
print("Problema Prático 4.9")
# Implemente a função meuGrep(), que toma como entrada duas strings, um nome de arquivo e uma string alvo, e exibe cada linha do arquivo que contém a string alvo como uma substring.
# meuGrep('example.txt', 'line')
# The 3 lines in this file end with the new line character.
# There is a blank line above this line.
def meuGrep(nomeDoArquivo, stringOcorrencia):
    'Exibir as linhas de um arquivo'
    arqEntrada = open(nomeDoArquivo, 'r')
    conteudo = arqEntrada.readlines()
    arqEntrada.close()
    for linha in conteudo:
        if stringOcorrencia in linha:
            print(linha)
meuGrep('example3.txt','horse')