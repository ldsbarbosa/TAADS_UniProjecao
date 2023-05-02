import math
def pontos(x,y,a,b):
    'x e y são os pontos iniciais; a e b são os pontos finais. Pense em um plano cartesiano'

    cateto1 = abs(x - a)
    cateto2 = abs(y - b)
    # Parte 1 -> Link de apoio: https://acervolima.com/inclinacao-de-uma-linha-reta-aula-11-de-matematica/
    if x - a == 0 or y - b == 0:
        inclinacao = 0
    else:
        inclinacao = (x - a) / (y - b)
    if inclinacao == 0:
        inclinacao = 'infinita'
    # Parte 2
    distancia = math.sqrt(cateto1**2 + cateto2**2)

    print("A inclinação é {} e a distância é {}".format(inclinacao,distancia))