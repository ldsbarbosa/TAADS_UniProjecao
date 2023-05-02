# Generated by Django 4.1.7 on 2023-03-18 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('idade', models.PositiveSmallIntegerField()),
                ('sexo', models.CharField(choices=[('Masculino', 'Masculino'), ('Feminino', 'Feminino')], max_length=15)),
                ('email', models.EmailField(max_length=30)),
                ('telefone', models.CharField(max_length=13)),
            ],
        ),
        migrations.CreateModel(
            name='CondicaoDeSaude',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('area', models.CharField(choices=[('Psicológico', 'Psicológico'), ('Psiquiátrico', 'Psiquiátrico'), ('Endocrinológico', 'Endocrinológico'), ('Nutricional', 'Nutricional'), ('Neurológico', 'Neurológico'), ('Físico', 'Físico')], max_length=15)),
                ('gravidade', models.PositiveSmallIntegerField(max_length=1)),
                ('idDoPaciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.paciente')),
            ],
        ),
    ]