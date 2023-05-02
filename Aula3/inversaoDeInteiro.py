import math
def inverte_int(inteiro):
    'inteiro deve ser um numero inteiro com tres digitos'
    qtdDigitos = int(math.log10(inteiro)) + 1
    inteiroInvertido = 0
    # inteiroInvertido  = (inteiro - (inteiro // 10 * 10)) * 100
    # inteiroInvertido += (inteiro // 10 - (inteiro // 100 * 10)) * 10
    # inteiroInvertido += (inteiro // 100 - (inteiro // 1000 * 10)) * 1
    # Após verificar o comportamento, refiz o código com for e incremento, implementando a lógica sugerida.
    for i in range(0,qtdDigitos):
        inteiroInvertido += (inteiro // 10**(qtdDigitos - i - 1) - (inteiro // 10**(qtdDigitos - i) * 10)) * 10**i

    return inteiroInvertido