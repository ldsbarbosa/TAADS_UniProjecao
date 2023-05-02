print("#########")
print("Problema Prático 1\n")
s1 = 'ant'
s2 = 'bat'
s3 = 'cod'
# Escreva expressões Python usando s1, s2 e s3 e os operadores + e * a fim de avaliar para:
# (a)
print("(a) "+" 'ant bat cod'")
print(s1 + ' ' + s2 + ' ' + s3)
# (b)
print("(b) "+" 'ant ant ant ant ant ant ant ant ant ant'")
print((s1 + ' ') * 9)
# (c)
print("(c) "+" 'ant bat bat cod cod cod'")
print(s1 + ' ' + ((s2 + ' ') * 2) + ((s3 + ' ') * 3))
# (d)
print("(d) "+" 'ant bat ant bat ant bat ant bat ant bat ant bat ant bat'")
print(7 * (s1 + ' '+ s2 + ' '))
# (e)
print("(e) "+" 'batbatcod batbatcod batbatcod batbatcod batbatcod'")
print(5 * (s2 + ' ' + s2 + ' '+ s3 + ' '))
print("####\n\n\n####")

# 
print("Problema Prático 2\n")
s = '0123456789'
#
# Agora, escreva expressões usando a string s e o operador de indexação
# (a)
print("(a) '0'")
print(s[0])
# (b)
print("(b) '1'")
print(s[1])
# (c)
print("(c) '6'")
print(s[6])
# (d)
print("(d) '8'")
print(s[8])
# (e)
print("(e) '9'")
print(s[9])
print("####\n\n\n####")