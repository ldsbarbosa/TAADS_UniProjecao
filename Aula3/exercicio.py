## 16 a 20
print('Exercícios')
print('\n####\n')
# Use a função eval() para avaliar essas strings como expressões Python:
print('Use a função eval() para avaliar essas strings como expressões Python:')
# (a)
print('(a)')
print(str(eval('2 * 3 + 1')))
# (b)
print('(b)')
# print(str(eval('hello'))) <- Dá erro pois hello não é uma expressão a ser avaliada. É uma string
# (c)
print('(c)')
print(str(eval("'hello' + 'not'+ 'world!'")))
# (d)
print('(d)')
print(str(eval("'ASCII'.count('I')")))
# (e)
print('(e)')
# print(str(eval('x = 5')))  <- Dá erro pois x = 5 não é uma expressão a ser avaliada. É uma atribuição de valor à uma variável
print("\n####\n")

# Suponha que a, b e c tenham sido definidas no shell interativo conforme mostrado:
print('Suponha que a, b e c tenham sido definidas no shell interativo conforme mostrado: a, b, c = 3, 4, 5')
a, b, c = 3, 4, 5
# (a)a for menor que b.
print('(a)')
if a < b:
    print("OK! a menor que b")
# (b)c for menor que b.
print('(b)')
if c < b:
    print("OK! c menor que b")
# (c)A soma de a e b for igual a c.
print('(c)')
if a + b == c:
    print("OK! a mais b é igual à c")
# (d)A soma dos quadrados de a e b for igual ao quadrado de c.
print('(d)')
if a**2 + b**2 == c**2:
    print("OK! A soma dos quadrados de a e b for igual ao quadrado de c")
print("\n####\n")

# Repita o exercício anterior com o requisito adicional de que 'NÃO OK' é exibido na tela se a condição for falsa.
print('Repita o exercício anterior com o requisito adicional de que \'NÃO OK\' é exibido na tela se a condição for falsa.')
a, b, c = 3, 4, 5
# (a)a for menor que b.
print('(a)')
if a < b:
    print("OK! a menor que b")
else:
    print("NÃO OK! a maior que b")
# (b)c for menor que b.
print('(b)')
if c < b:
    print("OK! c menor que b")
else:
    print("NÃO OK! c maior que b")
# (c)A soma de a e b for igual a c.
print('(c)')
if a + b == c:
    print("OK! a mais b é igual à c")
else:
    print("NÃO OK! a mais b é diferente de c")
# (d)A soma dos quadrados de a e b for igual ao quadrado de c.
print('(d)')
if a**2 + b**2 == c**2:
    print("OK! A soma dos quadrados de a e b é igual ao quadrado de c")
else:
    print("NÃO OK! A soma dos quadrados de a e b é diferente ao quadrado de c")
print("\n####\n")

# Escreva um laço for que percorra uma lista de strings lst e
# exiba os três primeiros caracteres de cada palavra.
print('Escreva um laço for que percorra uma lista de strings lst e exiba os três primeiros caracteres de cada palavra.')
lst = ['Janeiro', 'Fevereiro','Março','Abril','Maio','Junho','Julho']
for item in lst:
    print(item[0:3])
print("\n####\n")

# Escreva um laço for que percorre uma lista de números lst e
# exibe na tela os números na lista cujo quadrado seja divisível por 8.
# Por exemplo, se lst for [2, 3, 4, 5, 6, 7, 8, 9], então os números 4 e 8 devem ser exibidos.
lst = range(1,100)
print("Números os quais seus quadrados são divisíveis por 8")
for item in lst:
    if (item**2) % 8 == 0:
        print(item)
print("\n####\n")