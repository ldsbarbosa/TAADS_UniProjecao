primeiraPalavra = input('Digite a primeira palavra\n')
segundaPalavra = input('Digite a segunda palavra\n')
terceiraPalavra = input('Digite a terceira palavra\n')
listaDePalavrasInseridas = [primeiraPalavra,segundaPalavra,terceiraPalavra]
listaDePalavrasEmOrdem = listaDePalavrasInseridas[:]
listaDePalavrasEmOrdem.sort()
print('Lista de palavras digitadas: ',listaDePalavrasInseridas)
print('Lista de palavras em ordem: ',listaDePalavrasEmOrdem)
if listaDePalavrasInseridas == listaDePalavrasEmOrdem:
    print('Está em ordem')
else:
    print('Não está em ordem')