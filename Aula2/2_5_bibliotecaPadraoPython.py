import math
import fractions
##Problema Prático 1
#
print("#########")
print("Problema Prático 1")
print("\n----\n")
# Escreva expressões Python correspondentes ao seguinte:

#(a)
a = 3 # Cateto A
b = 4 # Cateto B
print("O comprimento da hipotenusa em um triângulo retângulo cujos dois outros lados têm comprimentos a e b")
print( str( math.sqrt(a**2 + b**2) ) + "\n")
#(b)
lst = [1,2,3]
print("O valor da expressão que avalia se o comprimento da hipotenusa acima é 5")
print(str( math.sqrt(a**2 + b**2) == 5 ) + "\n")
#(c)
print("A área de um disco com raio a")
print(str( math.pi * a**2 ) + "\n")
#(d)
print("O valor da expressão Booleana que verifica se um ponto com coordenadas x e y está dentro de um círculo com centro (a, b) e raio r")
print(str( (1 - a)**2 + (1 - b)**2 < 1**2 ) + "\n")
print("\n##########\n##########\n")
## Demonstração de Uso da Biblioteca Fractions
print("\nDemonstração de Uso da Biblioteca Fractions\n")

a = fractions.Fraction(3, 4)
b = fractions.Fraction(1, 2)

print(a)
print(b)
c = a + b
print("a + b = "+ str(c))