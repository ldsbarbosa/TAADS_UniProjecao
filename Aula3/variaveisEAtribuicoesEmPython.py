# Suponha que uma lista não vazia time foi atribuída. Escreva uma instrução Python ou instruções que mapeiam o primeiro e último valor da lista
time = ['Ava', 'Eleanor', 'Clare', 'Sarah']
print(time)
time[0], time[len(time)-1] = time[len(time)-1], time[0]
print(time)