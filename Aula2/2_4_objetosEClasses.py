##Problema Prático 1
#
print("#########")
print("Problema Prático 1")
print("\n----\n")
# Em que ordem os operadores nas expressões a seguir são avaliados?

#(a)
a = 0
print("2 + 3 == 4 or a >= 5")
print(str(2 + 3 == 4 or a >= 5) + "\n")
#(b)
lst = [1,2,3]
print("lst[1] * -3 < -10 == 0")
print(str(lst[1] * -3 < -10 == 0) + "\n")
#(c)
print("(lst[1] * -3 < -10) in [0, True]")
print(str((lst[1] * -3 < -10) in [0, True]) + "\n")
#(d)
print("2 * 3**2")
print(str(2 * 3**2) + "\n")
#(e)
print("4 / 2 in [1, 2, 3]")
print(str(4 / 2 in [1, 2, 3]) + "\n")
print("\n##########\n##########\n")

##Problema Prático 2
#
print("#########")
print("Problema Prático 2")
print("\n----\n")
# Qual é o tipo do objeto ao qual essas expressões são avaliadas?

#(a)
print("False + False")
print(str(False + False))
print(str(type(False + False)) + "\n")

#(b)
print("2 * 3**2.0")
print(str(2 * 3**2.0))
print(str(type(2 * 3**2.0)) + "\n")

#(c)
print("4 // 2 + 4 % 2")
print(str(4 // 2 + 4 % 2))
print(str(type(4 // 2 + 4 % 2)) + "\n")

#(d)
print("2 + 3 == 4 or 5 >= 5")
print(str(2 + 3 == 4 or 5 >= 5))
print(str(type(2 + 3 == 4 or 5 >= 5)) + "\n")
print("\n##########\n##########")