# 6.20 Escreva a função reverte(), que aceite como entrada uma agenda, ou seja, um dicionário mapeando nomes (as chaves)
# a números de telefone (os valores). A função deverá retornar outro dicionário representando a agenda reversa,
# mapeando números de telefone (as chaves) aos nomes (os valores).
import random, string


def reverte(agenda):
    outraAgenda = dict()
    for item in agenda.keys():
        outraAgenda[agenda[item]] = item
    return outraAgenda
# 6.21 Escreva a função símbolo() que aceite uma string (o nome de um arquivo) como entrada.
# O arquivo terá nomes de empresa e símbolos de ações.
# Nesse arquivo, um nome de empresa ocupará uma linha e seu símbolo de ação estará na linha seguinte.
# Após essa linha estará uma linha com outro nome de empresa e assim por diante.
# Seu programa lerá o arquivo e armazenará o nome e o símbolo da ação em um dicionário.
# Depois, ele fornecerá uma interface para o usuário, de modo que ele possa obter o símbolo da ação para determinada empresa.
# Teste seu código na lista NASDAQ 100 de ações, dada no arquivo nasdaq.txt.
# fonte: https://pt.wikipedia.org/wiki/NASDAQ-100
def simbolo(nomeDoArquivo):
    arquivo = open(nomeDoArquivo, 'r')
    linhasDoArquivo = arquivo.readlines()
    linhasDoArquivoDict = dict()
    for i in range(0,len(linhasDoArquivo),2):
        linhasDoArquivoDict[
                (linhasDoArquivo[i])[0:linhasDoArquivo[i].index('\n')]
            ] = (linhasDoArquivo[i+1])[0:linhasDoArquivo[i+1].index('\n')]
    while True:
        nomeDaEmpresa = input('Digite o nome da empresa: ')
        if nomeDaEmpresa == "":
            print("Você saiu do programa")
            break
        if nomeDaEmpresa in linhasDoArquivoDict:
            print(linhasDoArquivoDict[nomeDaEmpresa])
    arquivo.close()
    return
# 6.22 A imagem espelho da string vow é a string wov, e a imagem espelho de wood é a string boow.
# A imagem espelho da string bed, porém, não pode ser representada como uma string, pois a imagem espelho de e não é um caractere válido.
# Desenvolva a função espelho(), que apanhe uma string e retorne sua imagem espelho,
# mas somente se esta puder ser representada usando as letras no alfabeto.
def espelho(s):
    alfabeto = 'bdilmnopquvwx'
    stringInvertida = s[::-1]
    s_inv = []
    for i in range(len(stringInvertida)):
        s_inv.append(stringInvertida[i])
    
    for i in range(len(s_inv)):
        if s_inv[i] not in alfabeto:
            return 'Imagem espelho não pode ser representada'
        
        if s_inv[i] == 'b':
            s_inv[i] = 'd'
        elif s_inv[i] == 'd':
            s_inv[i] = 'b'
        elif s_inv[i] == 'p':
            s_inv[i] = 'q'
        elif s_inv[i] == 'q':
            s_inv[i] = 'p'
        
    return ''.join(s_inv)

def espelho2(s):
    alfabeto = 'bdilmnopquvwx'
    espelho_map = str.maketrans('bdilmnopquvwx', 'dbilmnoqpuxw')
    s_inv = s[::-1].translate(espelho_map)
    if set(s_inv) - set(alfabeto):
        # A diferença entre dois conjuntos contém todos os elementos
        # que estão no primeiro conjunto, mas não no segundo.
        return 'Imagem espelho não pode ser representada'
    return s_inv

# 6.23 Você gostaria de produzir um dicionário exclusivo assustador, mas tem dificuldade para achar milhares de palavras
# que deveriam entrar nesse dicionário. Sua ideia brilhante é escrever uma função dicAssust(),
# que leia uma versão eletrônica de um livro de terror, digamos, Frankenstein, de Mary Wollstonecraft Shelley,
# apanhe todas as palavras nele contidas e as escreva em ordem alfabética em um novo arquivo, chamado dicionário.txt.
# Você pode eliminar as palavras de uma e duas letras, pois nenhuma delas será assustadora.
# Você notará que a pontuação no texto torna esse exercício um pouco mais complicado.
# Você poderá tratar disso substituindo a pontuação por espaços ou strings vazias.
def dicAssust(nomeDoArquivo):
    arquivo = open(nomeDoArquivo, 'r')
    linhasDoArquivo = arquivo.readlines()
    palavras = []
    for l in linhasDoArquivo:
        for palavra in [*l.strip('\n').split(' ')]:
            if palavra != "":
                palavras.append(palavra)

    contador = 0
    for i in range(len(palavras)):
        for j in range(i+1,len(palavras)):
            palavra1 = (palavras[i])[contador]
            palavra2 = (palavras[j])[contador]
            while (ord(palavra1) == ord(palavra2) and
                   (contador < len(palavras[i]) - 1 and contador < len(palavras[j]) - 1)):
                contador+=1
                palavra1 = (palavras[i])[contador]
                palavra2 = (palavras[j])[contador]
            if ord(palavra1) > ord(palavra2):
                palavras[i], palavras[j] = palavras[j], palavras[i]
            contador = 0
    arquivo.close()
    return palavras

# 6.24 Implemente a função nomes(), que não aceite entrada, mas solicite repetidamente do usuário o nome de um estudante em uma turma.
# Quando o usuário digita a string vazia, a função deve exibir, para cada nome, o número de estudantes com esse nome.
def nomes():
    dicionario = dict()
    while True:
        nome = input("Digite o próximo nome: ")
        if nome == '':
            for nome in dicionario:
                print("Há {} aluno(s) chamado(s) {}".format(dicionario[nome], nome))   
            break     
        if nome in dicionario:
            dicionario[nome] += 1
        else:
            dicionario[nome] = 1
# 6.25 Escreva a função diferente(), que aceite uma tabela bidimensional como entrada e retorne o número de entradas distintas na tabela.
def diferente(tabela):
    entradasDistintas = []
    for linha in tabela:
        for num in linha:
            if num in entradasDistintas:
                continue
            else:
                entradasDistintas.append(num)
    return len(entradasDistintas)
# 6.26 Escreva a função semana(), que não aceita argumentos.
# Ela pedirá que o usuário informe repetidamente uma abreviação em três letras e sem acentuação para um dia da semana
# (Seg, Ter, Qua, Qui, Sex, Sab ou Dom), e depois imprimirá o dia correspondente no formato extenso.
def semana():
    dicionarioDias ={
        'Dom': 'Domingo',
        'Seg': 'Segunda-feira',
        'Ter': 'Terça-feira',
        'Qua': 'Quarta-feira',
        'Qui': 'Quinta-feira',
        'Sex': 'Sexta-feira',
        'Sab': 'Sábado',
    }
    abreviacao = input('Digite a abreação do dia: ')
    while abreviacao in dicionarioDias:
        print(dicionarioDias[abreviacao])
        abreviacao = input('Digite a abreação do dia: ')
# 6.27 Ao final deste livro (e em outros livros), normalmente existe um índice que relaciona as páginas em que certa palavra aparece.
# Neste problema, você criará um índice para um texto mas, em vez do número de páginas, você usará os números de linha.
# Você implementará a função índice(), que aceite como entrada o nome de um arquivo de texto e uma lista de palavras.
# Para cada palavra na lista, sua função achará as linhas no arquivo de texto em que a palavra ocorre,
# exibindo os números de linha correspondentes (onde a numeração começa com 1). Você deverá abrir e ler o arquivo apenas uma vez. 
def indice(nomeDoArquivo, lst):
    dicionarioPalavras = dict()
    for pal in lst:
        dicionarioPalavras[pal] = []

    arquivo = open(nomeDoArquivo, 'r')
    linhas = arquivo.readlines()
    for linha in linhas:
        linha = linha.strip('\n')
    
    for i in range(len(linhas)):
        for pal in lst:
            if pal in linhas[i]:
                dicionarioPalavras[pal].append(i)

    for pal in dicionarioPalavras:
        print("{:9}".format(pal),end=" ")
        print(dicionarioPalavras[pal])
# 6.28 Implemente a função traduza(), que ofereça um serviço de tradução rudimentar.
# A entrada da função é um dicionário mapeando palavras em um idioma (o primeiro idioma) às palavras correspondentes em outro
# (o segundo idioma). A função oferece um serviço que permite aos usuários digitar uma frase no primeiro idioma interativamente
# e depois obter uma tradução para o segundo idioma, pressionando a tecla Enter/Return.
# As palavras ausentes no dicionário devem ser traduzidas como _ _ _ _.
def traduza(dicionarioTraducao):
    while True:
        palavra = input('Insira a palavra a ser traduzida')
        if palavra == '':
            break
        if palavra in dicionarioTraducao.keys():
            print(dicionarioTraducao[palavra])
        else:
            for (chave, valor) in dicionarioTraducao.items():
                if palavra == valor:
                    print(chave)


# 6.29 Na sua turma, muitos estudantes são amigos. Vamos supor que dois estudantes que compartilham um amigo deverão ser amigos;
# em outras palavras, se os estudantes 0 e 1 são amigos e os estudantes 1 e 2 são amigos, então os estudantes 0 e 2 deverão ser amigos.
# Usando essa regra, podemos particionar os estudantes em círculos de amigos.
# Para fazer isso, implemente uma função redes(), que aceite dois argumentos de entrada.
# O primeiro é o número n de estudantes na turma. Consideramos que os estudantes são identificados usando os inteiros de 0 a n – 1.
# O segundo argumento de entrada é uma lista de objetos de tupla que define os amigos.
# Por exemplo, a tupla (0, 2) define os estudantes 0 e 2 como amigos. A função redes() deverá exibir a partição de estudantes em
# círculos de amigos, conforme ilustramos:

# algoritmo Union-Find -> Unir conjuntos disjuntos
def encontrar(pais, i):
    while i != pais[i]:
        pais[i] = pais[pais[i]]  # compressão de caminho
        i = pais[i]
    return i

def unir(pais, x, y):
    pai_x = encontrar(pais, x)
    pai_y = encontrar(pais, y)
    pais[pai_x] = pai_y

def redes(n, amizades):
    pais = list(range(n))
    for x, y in amizades:
        unir(pais, x, y)

    conjuntos = {}
    for i in range(n):
        raiz = encontrar(pais, i)
        if raiz not in conjuntos:
            conjuntos[raiz] = [i]
        else:
            conjuntos[raiz].append(i)

    for i, conjunto in enumerate(conjuntos.values()):
        print(f"Rede social {i}\tis {set(conjunto)}")

# 6.30 Implemente a função simul(), que aceite como entrada um inteiro n e simule n rodadas de Pedra, Papel e Tesoura
# entre os jogadores 1 e 2. O jogador que vencer mais rodadas vence o jogo de n rodadas, com possibilidade de empate. Sua função
# deverá exibir o resultado do jogo conforme mostramos. (Você pode querer usar sua solução do Problema 5.26.)
def pedraPapelTesoura(escolha):
    possibilidades = ('Pedra','Papel','Tesoura')
    if escolha not in possibilidades:
        return
    escolhaMaquina = possibilidades[random.randint(0,2)]
    if  (escolha == 'Pedra' and escolhaMaquina == 'Tesoura') or (escolha == 'Tesoura' and
         escolhaMaquina == 'Papel') or (escolha == 'Papel' and escolhaMaquina == 'Pedra'):
        return 1
    elif (escolhaMaquina == 'Pedra' and escolha == 'Tesoura') or (escolhaMaquina == 'Tesoura' and
         escolha == 'Papel') or (escolhaMaquina == 'Papel' and escolha == 'Pedra'):
        return -1
    else:
        return 0

def simul(numero):
    partidas = []
    resultado = []
    possibilidades = ('Pedra','Papel','Tesoura')

    contador = 0
    while contador < numero:
        partidas.append(pedraPapelTesoura(possibilidades[random.randint(0,2)]))
        contador+=1

    for i in range(len(possibilidades)): ## A possibilidade de jogadas coincide com as possibilidades de resultado de uma partida
        resultado.append(partidas.count(i - 1))
    if resultado[0] > resultado[2]:
        print("Máquina ganhou (Jogador 2). Placar: {} - {}".format(resultado[0],resultado[2]))
    elif resultado[0] < resultado[2]:
        print("Você ganhou (Jogador 1). Placar: {} - {}".format(resultado[0],resultado[2]))
    else:
        print("Empate. Placar: {} - {}".format(resultado[0],resultado[2]))
# 6.31 Craps é um jogo baseado em dados, popular em muitos cassinos. Assim como blackjack, um jogador joga contra a casa.
# O jogo começa com o jogador lançando um par de dados comum, com seis lados. Se o jogador resultar em um total de 7 ou 11, ele vence.
# Se o jogador totalizar 2, 3 ou 12, ele perde. Para todos os outros resultados, o jogador lançará repetidamente o par de dados até
# que consiga o valor inicial novamente (quando ganhará) ou 7 (quando perderá).
def craps():
    dado = [1,2,3,4,5,6]
    jogador = 0
    while jogador not in [2, 3, 7, 11, 12]:
        jogador = dado[random.randint(0,5)] + dado[random.randint(0,5)]
        if jogador in [7, 11]:
            return 1
        if jogador in [2, 3, 12]:
            return 0
        
def testaCraps(numero):
    contador = 0
    contadorResultados = []
    while contador < numero:
        contadorResultados.append(craps())
        contador+=1
    return contadorResultados.count(1) / len(contadorResultados)
# 6.32 Você poderá saber que as ruas e avenidas de Manhattan (Nova York) formam uma grade. Um percurso aleatório pela grade (isto é, Manhattan)
# é um percurso em que uma direção aleatória (N, S, L, O) é escolhida com a mesma probabilidade em cada interseção.
# Por exemplo, um percurso aleatório em uma grade de 5 × 11 começando em (5,2) poderia visitar os pontos (6, 2), (7, 2), (8, 2),
# (9, 2), (10, 2), de volta a (9, 2) e depois de volta a (10, 2), antes de sair da grade.
# Escreva a função manhattan(), que apanha o número de linhas e colunas na grade, simula um percurso aleatório começando no centro da grade e calcula o número de vezes que cada interseção foi visitada pelo percurso aleatório. Sua função deverá exibir a tabela linha por linha quando o percurso aleatório se mover para fora da grade.
def manhattan(linhas, colunas):
    # Onde começa
    linhaInicial = linhas // 2
    colunaInicial = colunas // 2

    # Gerando grade
    grade = []
    for linha in range(linhas):
        grade.append([])
    for g in grade:
        for coluna in range(colunas):
            g.append(0)
    grade[linhaInicial][colunaInicial] = 1

    #Movimentação aleatoria
    for i in range(0,random.randint(7,14)):
        movimento = [random.randint(0,1),random.randint(0,1)]
        
        if linhaInicial == 0 and movimento[0] == 0:
            movimento[0] = 1        
        if colunaInicial == 0 and movimento[1] == 0:
            movimento[1] = 1
        
        if (linhaInicial == len(grade) - 1) and movimento[0] == 1:
            movimento[0] = 0
        if (colunaInicial == len(grade[0]) - 1) and movimento[1] == 1:
            movimento[1] = 0        

        if movimento[0] == 0:
            linhaInicial-=1
        else:
            linhaInicial+=1
        
        if movimento[1] == 0:
            colunaInicial-=1
        else:
            colunaInicial+=1
        
        grade[linhaInicial][colunaInicial] += 1
    for g in grade:
        print(g)

# 6.33 O jogo de cartas para dois jogadores War é jogado com um baralho comum de 52 cartas. Um baralho misturado é dividido igualmente entre os dois jogadores, que mantêm suas cartas viradas para baixo. O jogo consiste em batalhas, até que um dos jogadores esgote suas cartas. Em uma batalha, cada jogador revela a carta do topo de sua pilha; o jogador com a carta mais alta toma as duas cartas e as vira para baixo no fundo de sua pilha. Se as duas cartas tiverem o mesmo valor, ocorre uma guerra.
# Em uma guerra, cada jogador coloca, virada para baixo, suas três cartas de cima e escolhe uma delas. O jogador que escolher a carta de maior valor acrescenta todas as oito cartas no fundo de sua pilha. No caso de outro empate, as guerras são repetidas, até que um jogador vença e coleta todas as cartas sobre a mesa. Se um jogador ficar sem cartas antes de virar as três cartas em uma guerra, eles poderão concluir a guerra, usando sua última carta como escolha.
# Em War, o valor de uma carta de número é o seu próprio valor posicional, e os valores das cartas com letras A, K, Q e J são 14, 13, 12 e 11, respectivamente.
# (a)Escreva uma função war(), que simule um jogo de War e retorne uma tupla contendo o número de batalhas, guerras e guerras de duas rodadas no jogo. Nota: ao incluir cartas ao fundo da pilha de um jogador, não se esqueça de embaralhar as cartas primeiro, para gerar mais aleatoriedade à simulação.
# (b)Escreva uma função warStats(), que aceite um inteiro positivo n como entrada, simule n jogos de War e calcule o número médio de batalhas, guerras e guerras de duas rodadas.
def war():
    baralho = [(n, v) for n in range(2, 11) for v in ('Paus', 'Ouros', 'Copas', 'Espadas')] + [(n, v) for n in (11, 12, 13, 14) for v in ('Paus', 'Ouros', 'Copas', 'Espadas')]
    random.shuffle(baralho)

    jogador1 = baralho[:26]
    jogador2 = baralho[26:]

    batalhas = 0
    guerras = 0
    guerras_2rodadas = 0

    while jogador1 and jogador2:
        batalhas += 1
        carta1 = jogador1.pop(0)
        carta2 = jogador2.pop(0)

        if carta1[0] > carta2[0]:
            jogador1 += [carta1, carta2]
        elif carta2[0] > carta1[0]:
            jogador2 += [carta1, carta2]
        else:
            guerras += 1
            mao1 = [carta1] + jogador1[:3]
            mao2 = [carta2] + jogador2[:3]
            del jogador1[:3]
            del jogador2[:3]

            if mao1[-1][0] > mao2[-1][0]:
                jogador1 += mao1 + mao2
            elif mao2[-1][0] > mao1[-1][0]:
                jogador2 += mao1 + mao2
            else:
                guerras_2rodadas += 1
                mao1 += jogador1[:3]
                mao2 += jogador2[:3]
                del jogador1[:3]
                del jogador2[:3]

                if mao1[-1][0] > mao2[-1][0]:
                    jogador1 += mao1 + mao2
                else:
                    jogador2 += mao1 + mao2

    return (batalhas, guerras, guerras_2rodadas)


def warStats(n):
    total_battles = 0
    total_wars = 0
    total_double_wars = 0
    
    for i in range(n):
        battles, wars, double_wars = war()
        total_battles += battles
        total_wars += wars
        total_double_wars += double_wars
    
    avg_battles = total_battles / n
    avg_wars = total_wars / n
    avg_double_wars = total_double_wars / n
    
    print("Média de batalhas:", avg_battles)
    print("Média de guerras:", avg_wars)
    print("Média de guerras de duas rodadas:", avg_double_wars)

# 6.34 Desenvolva um jogo simples que ensine a alunos de jardim da infância a somar números de um dígito.
# Sua função jogo() apanhará um inteiro n como entrada e depois fará n perguntas de adição com números de único dígito.
# Os números a serem somados deverão ser escolhidos aleatoriamente a partir do intervalo [0, 9] (isto é, 0 a 9, inclusive).
# O usuário informará a resposta quando solicitado. Sua função deverá exibir 'Correto' ou 'Incorreto',
# dependendo se a resposta é correta ou não. Depois de n perguntas, sua função deverá exibir o número de respostas corretas.
# >>> jogo(3)
# 8 + 2 =
# Digite a resposta: 10
# Correto.
# 6 + 7 =
# Digite a resposta: 12
# Incorreto.
# 7 + 7 =
# Digite a resposta: 14
# Correto.
# Você teve 2 respostas corretas entre 3
def jogo(numero):
    contador = 0
    for i in range(numero):
        num1, num2 = random.randint(0,9), random.randint(0,9)
        print("{} + {}".format(num1, num2))
        resposta = int(input('Digite a resposta: '))
        if resposta == num1 + num2:
            contador+=1
            print("Correto!")
        else:
            print("Incorreto.")
    print("Você teve {} respostas correstas entre {}".format(contador, numero))
# 6.35 A cifra de César é uma técnica de criptografia em que cada letra da mensagem é substituída pela letra que é um número fixo de posições no alfabeto. Esse “número fixo” é chamado de chave, que pode ter qualquer valor de 1 a 25. Se a chave for 4, por exemplo, então a letra A seria substituída por E, B por F, C por G e assim sucessivamente. Os caracteres no final do alfabeto, W, X, Y e Z, seriam substituídos por A, B, C e D.
# Escreva a função césar(), que aceite como entrada uma chave entre 1 e 25 e um nome de arquivo de texto (uma string). Sua função deverá codificar o conteúdo do arquivo com uma cifra de César usando a chave de entrada e gravar o conteúdo codificado em um novo arquivo cifra.txt (além de retorná-lo).
# Arquivo: clear.txt
# >>> césar(3, 'clear.txt')
# "Vsb Pdqxdo (Wrs vhfuhw)\n\n1. Dozdbv zhdu d gdun frdw.\n2. Dozdbv
# zhdu brxu djhqfb'v edgjh rq brxu frdw.\n"
def cesar(chave, nomeDoArquivo):
    arquivo = open(nomeDoArquivo, 'r')
    linhas = arquivo.readlines()
    arquivo.close()
    linhasCriptografadas = []
    linhaUnicaCritpo = ""
    for linha in linhas:
        for c in linha:
            if c.islower():
                if (ord(c) + chave) > ord('z'):
                    linhaUnicaCritpo += chr(ord(c) + chave -25)
                else:
                    linhaUnicaCritpo += chr(ord(c) + chave)
            else:
                if (ord(c) + chave) > ord('Z'):
                    linhaUnicaCritpo += chr(ord(c) + chave - 25)
                else:
                    linhaUnicaCritpo += chr(ord(c) + chave)
        linhasCriptografadas.append(linhaUnicaCritpo)
        linhaUnicaCritpo = ""
    arquivo = open(nomeDoArquivo, 'w')
    arquivo.writelines(linhasCriptografadas)
    arquivo.close()
    return linhasCriptografadas
# 6.36 George Kingsley Zipf (1902-1950) observou que a frequência da k-ésima palavra mais comum em um texto é aproximadamente proporcional a 1/k. Isso significa que há um valor constante C tal que, para a maioria das palavras w no texto, o seguinte é verdadeiro:
# Se a palavra w é a k-ésima mais comum, então freq(w)* k ≈ C
# Aqui, pela frequência da palavra w, freq(w), queremos dizer o número de vezes que a palavra ocorre no texto dividido pelo número total de palavras no texto.
# Implemente a função zipf(), que aceite um nome de arquivo como entrada e verifique a observação de Zipf, exibindo o valor freq(w)*k para as 10 primeiras palavras mais frequentes w no arquivo. Ao processar o arquivo, ignore o uso de maiúsculas e minúsculas, assim como a pontuação.
# Arquivo: frankenstein.txt
# >>> zipf('frankenstein.txt')
# 0.0557319552019
# 0.0790477076165
# 0.113270715149
# 0.140452498306
# 0.139097394747
# 0.141648177917
# 0.129359248582
# 0.119993091629
# 0.122078888284
# 0.134978942754
def zipf(filename):
    # Passo 1
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read().lower().translate(str.maketrans('', '', string.punctuation))
        words = text.split()

    # Passo 2
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1

    # Passo 3
    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    # Passo 4
    for i in range(10):
        word, f = sorted_freq[i]
        print(f * (i+1))