# Generated by Django 4.1.7 on 2023-03-18 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_condicaodesaude_gravidade'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='CPF',
            field=models.CharField(max_length=14),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paciente',
            name='data_de_nascimento',
            field=models.DateField(),
            preserve_default=False,
        ),
    ]
