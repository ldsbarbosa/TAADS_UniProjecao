
##Problema Prático 1
#
print("#########")
print("Problema Prático 1\n")
palavras = ['taco', 'bola', 'celeiro', 'cesta', 'peteca']
# Agora, escreva duas expressões Python que são avaliadas, respectivamente,
# como a primeiro e a última palavras em palavras, na ordem do dicionário.
palavras.sort()
print("Primeira palavra: "+palavras[0])
print("Última palavra: "+palavras[4])

print("\n##########\n")
print("Problema Prático 2\n")
notas = [9, 7, 7, 10, 3, 9, 6, 6, 2]
# (a)
print("(a)Uma expressão que avalia para o número de 7 notas.")
print(len(notas))
notas.pop()
notas.pop()
print(len(notas))
print("\n")
# (b)
print("(b)Uma instrução que muda a última nota para 4.")
print(notas[len(notas) - 1])
notas[len(notas) - 1] = 4;
print(notas[len(notas) - 1])
print("\n")
# (c)
print("(c)Uma expressão que avalia para a nota mais alta.")
print(max(notas))
print("\n")
# (d)
print("(d)Uma instrução que classifica as notas da lista.")
print(notas)
notas.sort()
print(notas)
print("\n")
# (e)
print("(e)Uma expressão que avalia para a média das notas.")
media = str(sum(notas) / len(notas))
print(notas)
print("Media das notas: " + media)
print("\n")
print("#########")