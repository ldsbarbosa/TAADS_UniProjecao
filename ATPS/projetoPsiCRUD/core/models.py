from django.db import models

class Paciente(models.Model):
    MASCULINO = 'Masculino'
    FEMININO = 'Feminino'
    SEXO_CHOICES = [
        (MASCULINO, 'Masculino'),
        (FEMININO, 'Feminino')
    ]

    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14) # 000.000.000-00
    data_de_nascimento = models.DateField()
    idade = models.PositiveSmallIntegerField()
    sexo = models.CharField(max_length=15, choices=SEXO_CHOICES)
    email = models.EmailField(max_length=30)
    telefone = models.CharField(max_length=13) # 61 99000-1111

class CondicaoDeSaude(models.Model):
    PSICOLOGICO = 'Psicológico'
    PSIQUIATRICO = 'Psiquiátrico'
    ENDOCRINOLOGICO = 'Endocrinológico'
    NUTRICIONAL = 'Nutricional'
    NEUROLOGICO = 'Neurológico'
    FISICO = 'Físico'
    AREA_CHOICES = [
        (PSICOLOGICO, 'Psicológico'),
        (PSIQUIATRICO, 'Psiquiátrico'),
        (ENDOCRINOLOGICO, 'Endocrinológico'),
        (NUTRICIONAL, 'Nutricional'),
        (NEUROLOGICO, 'Neurológico'),
        (FISICO, 'Físico')
    ]
    nome = models.CharField(max_length=100)
    idDoPaciente = models.ForeignKey(
        'Paciente',
        on_delete=models.CASCADE,
    )
    descricao = models.TextField()
    area = models.CharField(max_length=15, choices=AREA_CHOICES)
    gravidade = models.PositiveSmallIntegerField() # Gravidade de 0 a 10