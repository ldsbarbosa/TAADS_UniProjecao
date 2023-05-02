# Problema Prático 6.9
# Implemente a função adivinhe(), que aceita como entrada um inteiro n e implementa um jogo interativo
# de adivinhação de números.
# A função deverá começar escolhendo um número aleatório no intervalo de 0 até n,
# mas não incluindo este. A função, então, pedirá repetidamente ao usuário
# para adivinhar o número escolhido. Quando o usuário adivinhar corretamente,
# a função deverá exibir uma mensagem 'Acertou!' e terminar.
# Toda vez que o usuário escolhe um número incorreto,
# a função deverá ajudá-lo exibindo a mensagem 'Muito baixo' ou 'Muito alto'.
import random

def adivinhe(numeroMaximo):
    numeroAleatorio = random.randint(0,numeroMaximo)
    tentativa = int(input('Digite seu número: '))
    while tentativa != numeroAleatorio:
        if tentativa > numeroAleatorio:
            print('Muito alto.')
        else:
            print('Muito baixo')
        tentativa = int(input('Digite seu número: '))
    print('Acertou!')

# Problema Prático 6.10
# Existe uma forma de estimar o valor da constante matemática p lançando dardos em um alvo.
# Essa não é uma boa maneira de estimar p, mas é divertida. Suponha que você tenha um circulo com raio 1
# dentro de um quadrado de 2 × 2 na parede. Agora, lance os
# dardos aleatoriamente e suponha que, de n dardos que atingem o quadrado, k atinjam o alvo (veja a Figura 6.6).

def aproxPi(numeroDardos):
    PROBABILIDADE_ATINGIR_CIRCULO = 0.785
    PROBABILIDADE_ATINGIR_QUADRADO = 1 # Sempre que um dardo for lançado, ele atingirá o quadrado
    k = 0
    for i in range(numeroDardos):
        atingiu = random.uniform(0,1) # Lança
        if atingiu <= 0.785: # Confere se o lançamento está dentro do circulo
            k += 1
    return (4 * k) / numeroDardos