def inverteNome(nome):
    primeiroNome = nome.split()[0]
    primeiroNome = primeiroNome[0] + "."
    segundoNome = nome.split()[1]
    print(segundoNome + " " + primeiroNome)