def ion2e(nome):
    if nome.find('ion') != -1:
        nome = nome.replace('ion','e')
    return nome