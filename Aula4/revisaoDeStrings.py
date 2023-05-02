# Problema Prático 4.1
print("Problema Prático 4.1")
# Comece executando a atribuição:
s = '0123456789'
# Agora, escreva expressões (usando s e o operador de indexação) que sejam avaliadas como:
# (a)'234'
print(s[2:5])
# (b)'78'
print(s[7:9])
# (c)'1234567'
print(s[1:8])
# (d)'0123'
print(s[0:4])
# (e)'789'
print(s[7:10])

print("\n###\n###\n")
# Problema Prático 4.2
print("Problema Prático 4.2")
# Supondo que a variável previsão tenha recebido a string
previsao = 'It will be a sunny day today'
# escreva instruções Python correspondentes a estas atribuições:
#(a)À variável cont, a quantidade de ocorrências da string 'day' na string previsão.
cont = previsao.count('day')
print(cont)
#(b)À variável clima, o índice em que a substring 'sunny' começa.
clima = previsao.index('sunny')
print(clima)
#(c)À variável troca, uma cópia de previsão na qual cada ocorrência da substring 'sunny' é substituída por 'cloudy'.
troca = previsao.replace('sunny','cloudy')
print(troca)