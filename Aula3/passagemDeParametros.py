# Implemente a função trocaPU(), que aceita uma lista como entrada e troca o primeiro e último elementos da lista.
# Você pode considerar que a lista não estará vazia. A função não deverá retornar nada.
def trocaPU(lst):
    lst[0], lst[len(lst)-1] = lst[len(lst)-1], lst[0]
    print(lst)