def pagar(salarioHora, horasTrabalhadas):
    if horasTrabalhadas > 40:
        return int((salarioHora * 40) + (salarioHora * 1.5 * (horasTrabalhadas - 40)))
    else:
        return salarioHora * horasTrabalhadas