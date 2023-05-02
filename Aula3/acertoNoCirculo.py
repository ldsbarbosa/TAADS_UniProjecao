import math

def acerto(x, y, raioC, a, b):
    acertou = True
    reta1 = abs(x - a)
    reta2 = abs(y - b)

    if reta1 == 0 or reta2 == 0:
        if (reta1 > raioC) or (reta2 > raioC):
            acertou = False
    else:
        distancia = math.sqrt(reta1**2 + reta2**2)
        if distancia > raioC:
            acertou = False
    return acertou