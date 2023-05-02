#Problema Prático 6.1
#Escreva uma função estadoNasc() que aceite como entrada o nome completo de um presidente dos Estados Unidos (como uma string) e retorne o estado em que ele nasceu. Você deverá usar esse dicionário para armazenar o estado em que cada presidente recente nasceu:

def estadoNasc(pessoa):
    presidenteNascimento = {
        'Barack Hussein Obama II':'Hawaii',
        'George Walker Bush':'Connecticut',
        'William Jefferson Clinton':'Arkansas',
        'George Herbert Walker Bush':'Massachussetts',
        'Ronald Wilson Reagan':'Illinois',
        'James Earl Carter, Jr':'Georgia'
    }
    for presidente in presidenteNascimento:
        if presidente == pessoa:
            print(presidenteNascimento[presidente])
            break

#Problema Prático 6.2
#Implemente a função rlookup(), que oferece o recurso de pesquisa reversa de uma agenda de telefones. Sua função aceita, como entrada, um dicionário representando uma agenda de telefones. No dicionário, os números de telefone (chaves) são mapeados para indivíduos (valores). Sua função deverá oferecer uma interface de usuário simples, por meio da qual um usuário pode inserir um número de telefone e obter o nome e sobrenome do indivíduo atribuído a esse número.

def rlookup(dicionario):
    telefoneSolicitado = input('Digite número do telefone no formato (xxx)xxx-xx-xx: ')
    algumTelefone = False
    for tel in dicionario:
        if tel == telefoneSolicitado:
            algumTelefone = True
            print(dicionario[telefoneSolicitado])
    if not algumTelefone:
        print('O número informado não está em uso.')

# Implemente a função contaPalavra(), que aceite como entrada um texto — como uma string —
# e exiba a frequência de cada palavra no texto.
# Você pode considerar que o texto não possui pontuação e que as palavras são separadas por espaços em branco.
def contaPalavra(texto):
    contador = {}
    palavras = texto.split(' ')

    for palavra in palavras:
        if palavra in contador:
            contador[palavra] += 1
        else:
            contador[palavra] = 1

    for palavra in contador:
        if contador[palavra] == 1:
            print("{}\t appears {} time.".format(palavra, contador[palavra]))
        else:
            print("{}\t appears {} times.".format(palavra, contador[palavra]))
