import math

def colisao(x,y,raio1,a,b,raio2):
    colidiu = False
    cateto1 = abs(x - a)
    cateto2 = abs(y - b)
    
    if cateto1 == 0 or cateto2 == 0:
        if (cateto1 < raio1 + raio2) or (cateto2 < raio1 + raio2):
            colidiu = True
    else:
        distancia = math.sqrt(cateto1**2 + cateto2**2)
        if distancia < raio1 + raio2:
            colidiu = True

    return colidiu