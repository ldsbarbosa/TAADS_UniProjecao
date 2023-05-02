import time

def openLog(nomearq, modo = 'r'):
    '''abre arquivo nomearq em certo modo e retorna referência ao
    arquivo aberto; registra o acesso ao arquivo em log.txt'''
    
    arqEntrada = open(nomearq, modo)
    
    agora = time.localtime()
    agoraFormatado = time.strftime('%A %b/%d/%y %I:%M %p', agora)
    arqSaída = open('log.txt', 'a')
    log = '{}: Arquivo {} aberto.\n'
    arqSaída.write(log.format(agoraFormatado, nomearq))
    arqSaída.close()
    
    return arqEntrada