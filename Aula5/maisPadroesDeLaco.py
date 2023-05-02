# Sabe-se que o valor exato de e é igual a esta soma infinita:
# Uma soma infinita é impossível de ser calculada.
# Podemos conseguir uma aproximação de e calculando a soma dos primeiros poucos termos na soma infinita.
# Por exemplo, é uma aproximação (grosseira) para e.
# A próxima soma, , é melhor, mas ainda muito ruim. A próxima, , parece ser melhor. As próximas somas mostram que estamos seguindo na direção correta:
# Agora, como  ..., sabemos que e4 está dentro de  do valor real para e. Isso nos dá um modo de calcular uma aproximação de e que esteja garantidamente dentro de determinado intervalo do valor verdadeiro de e.
# Escreva a função aproxE() que aceita como entrada um valor de ponto flutuante erro e retorna um valor que aproxima a constante e até dentro do erro. Você fará isso gerando a sequência de aproximação e0, e1, e2, …, até que a diferença entre a aproximadamente atual e a anterior não seja maior que o erro.

from math import factorial


def aproxE(erro):
    'retorna aproximação de e dentro do erro'
    ant = 1 
    atual = 2 
    i = 2 
    while atual-ant > erro:
        ant = atual 
        atual = ant + 1/factorial(i) 
        i += 1 
    return atual