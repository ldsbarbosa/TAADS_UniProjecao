# Generated by Django 4.1.7 on 2023-03-18 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_paciente_cpf_paciente_data_de_nascimento'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paciente',
            old_name='CPF',
            new_name='cpf',
        ),
    ]