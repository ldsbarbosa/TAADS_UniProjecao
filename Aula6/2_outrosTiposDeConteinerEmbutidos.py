# Problema Prático 6.5
# Use a função lookup()para implementar uma aplicação de pesquisa de agenda.
# Sua função aceita, como entrada, um dicionário representando uma agenda. No dicionário, as tuplas contendo nomes e sobrenomes de indivíduos (as chaves) são mapeadas a strings contendo números de telefone (os valores). Veja aqui um exemplo:
# >>> agenda = {('Anna','Karenina'):'(123)456-78-90',
#               ('Yu', 'Tsun'):'(901)234-56-78',
#               ('Hans', 'Castorp'):'(321)908-76-54'}
# Sua função deverá oferecer uma interface simples com o usuário,
# por meio da qual ele possa informar o nome e sobrenome de um indivíduo 
# e obter o número de telefone atribuído a esse indivíduo.
def lookup(agenda):
    nome = input('Digite o nome: ')
    sobrenome = input('Digite o sobrenome: ')
    for nomeSobrenome in agenda.keys():
        if nomeSobrenome == (nome, sobrenome):
            print(agenda[(nome, sobrenome)])
            break

# Problema Prático 6.6
# Implemente a função sync() que aceita uma lista de agendas
# (em que cada agenda é um conjunto de números de telefone)
# como entrada e retorna uma agenda (como um conjunto) contendo a união de todas as agendas.
def sync(listaDeAgendas):
    totalAgendas = set()
    for agenda in listaDeAgendas:
        totalAgendas = totalAgendas | agenda
    return totalAgendas