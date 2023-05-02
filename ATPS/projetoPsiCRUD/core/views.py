from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from core.utils import GeraPDF
from .models import Paciente, CondicaoDeSaude
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
from django.views.generic import View
import re
import datetime

## Funções extras
def calcularIdade(dataDeNascimento): 
    hoje = datetime.date.today() 
    idade = hoje.year - dataDeNascimento.year - ((hoje.month, hoje.day) < 
         (dataDeNascimento.month, dataDeNascimento.day)) 
    return idade

class ListaPacientesPdfView(View, GeraPDF):
    def get(request, *args, **kwargs):
        pacientes = Paciente.objects.all()
        dados = {
            'pacientes': pacientes,
        }
        pdf = GeraPDF
        return pdf.render_to_pdf('core/pacientes.html',dados)

class ListaCondicoesDeSaudePdfView(View, GeraPDF):
    def get(self, request, id_paciente, *args, **kwargs):
        if id_paciente is None:
            return HttpResponse("Não há paciente com esse id. Tente novamente.")
        condicoesDeSaude = CondicaoDeSaude.objects.filter(idDoPaciente_id=id_paciente)
        paciente = Paciente.objects.get(id=id_paciente)
        dados = {
            'paciente': paciente,
            'condicoesDeSaude': condicoesDeSaude,
        }
        pdf = GeraPDF
        return pdf.render_to_pdf('core/condicoesdesaude.html',dados)

## Paciente
@login_required(login_url="/core/autenticacao")
def home(request): # Form e Read via Table de Pacientes
    pacientes = Paciente.objects.all()
    return render(request, 'index.html',{'pacientes': pacientes})

@login_required(login_url="/core/autenticacao")
def salvar_paciente(request):
    nome = request.POST.get("nome")
    ## idade = int(request.POST.get("idade"))
    sexo = request.POST.get("sexo")
    email = request.POST.get("email")
    telefone = request.POST.get("telefone")
    cpf = request.POST.get("cpf")
    data_de_nascimento = request.POST.get("data_de_nascimento")
    data_de_nascimento = datetime.datetime.strptime(data_de_nascimento, '%Y-%m-%d')
    idade = calcularIdade(data_de_nascimento)
    
    if idade > 150 or idade < 5:
        return render(request, 'index.html',{
            'pacientes': pacientes,
            'retorno_salvar': 'A idade não pode ser maior do que 150'
        })
    
    if sexo != 'Masculino' and sexo != 'Feminino':
        return render(request, 'index.html',{
            'pacientes': pacientes,
            'retorno_salvar': 'O sexo ou é masculino ou é feminino'
        })
    
    if re.match("([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+", email) is None:
        return render(request, 'index.html',{
            'pacientes': pacientes,
            'retorno_salvar': 'O email é inválido'
        })

    if re.match("([0-9]{2}) ([0-9]{4,5})-([0-9]{4})", telefone) is None:
        return render(request, 'index.html',{
            'pacientes': pacientes,
            'retorno_salvar': 'O telefone é inválido'
        })

    if re.match("^([0-9]{3}[.][0-9]{3}[.][0-9]{3}[-][0-9]{2})$", cpf) is None:
        return render(request, 'index.html',{
            'pacientes': pacientes,
            'retorno_salvar': 'O CPF é inválido'
        })
    else:
        cpfValido = [int(char) for char in cpf if char.isdigit()]
        if len(cpfValido) != 11:
            return render(request, 'index.html',{
                'pacientes': pacientes,
                'retorno_salvar': 'O CPF é inválido'
            })

        if cpfValido == cpfValido[::-1]:
            return render(request, 'index.html',{
                'pacientes': pacientes,
                'retorno_salvar': 'O CPF é inválido'
            })

        for i in range(9, 11):
            valor = sum((cpfValido[numero] * ((i+1) - numero) for numero in range(0, i)))
            digito = ((valor * 10) % 11) % 10
            if digito != cpfValido[i]:
                return render(request, 'index.html',{
                    'pacientes': pacientes,
                    'retorno_salvar': 'O CPF é inválido'
                })
    
    
    Paciente.objects.create(nome=nome,
                            idade=idade,
                            sexo=sexo,
                            email=email,
                            telefone=telefone,
                            cpf=cpf,
                            data_de_nascimento=data_de_nascimento.strftime("%Y-%m-%d"))
    pacientes = Paciente.objects.all()
    return render(request, 'index.html',{
                    'pacientes': pacientes,
                    'retorno_salvar': 'Operação de criação bem-sucedida!'
                })

@login_required(login_url="/core/autenticacao")
def alterar_paciente(request, id):
    paciente = Paciente.objects.get(id=id)
    paciente.data_de_nascimento = (paciente.data_de_nascimento).strftime("%Y-%m-%d")
    return render(request, "alteracao_paciente.html",{"paciente":paciente})

@login_required(login_url="/core/autenticacao")
def excluir_paciente(request, id):
    paciente = Paciente.objects.get(id=id)
    paciente.delete()
    return redirect(home)

@login_required(login_url="/core/autenticacao")
def editar_paciente(request, id):    
    nome = request.POST.get("nome")
    ## idade = int(request.POST.get("idade"))
    sexo = request.POST.get("sexo")
    email = request.POST.get("email")
    telefone = request.POST.get("telefone")
    cpf = request.POST.get("cpf")
    data_de_nascimento = request.POST.get("data_de_nascimento")
    data_de_nascimento = datetime.datetime.strptime(data_de_nascimento, '%Y-%m-%d')
    idade = calcularIdade(data_de_nascimento)
    
    if idade > 150 or idade < 5:
        return render(request, 'index.html',{
            'pacientes': pacientes,
            'retorno_salvar': 'A idade não pode ser maior do que 150'
        })
    
    if sexo != 'Masculino' and sexo != 'Feminino':
        return render(request, 'index.html',{
            'pacientes': pacientes,
            'retorno_salvar': 'O sexo ou é masculino ou é feminino'
        })
    
    if re.match("([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+", email) is None:
        return render(request, 'index.html',{
            'pacientes': pacientes,
            'retorno_salvar': 'O email é inválido'
        })

    if re.match("([0-9]{2}) ([0-9]{4,5})-([0-9]{4})", telefone) is None:
        return render(request, 'index.html',{
            'pacientes': pacientes,
            'retorno_salvar': 'O telefone é inválido'
        })

    if re.match("^([0-9]{3}[.][0-9]{3}[.][0-9]{3}[-][0-9]{2})$", cpf) is None:
        return render(request, 'index.html',{
            'pacientes': pacientes,
            'retorno_salvar': 'O CPF é inválido'
        })
    else:
        cpfValido = [int(char) for char in cpf if char.isdigit()]
        if len(cpfValido) != 11:
            return render(request, 'index.html',{
                'pacientes': pacientes,
                'retorno_salvar': 'O CPF é inválido'
            })

        if cpfValido == cpfValido[::-1]:
            return render(request, 'index.html',{
                'pacientes': pacientes,
                'retorno_salvar': 'O CPF é inválido'
            })

        for i in range(9, 11):
            valor = sum((cpfValido[numero] * ((i+1) - numero) for numero in range(0, i)))
            digito = ((valor * 10) % 11) % 10
            if digito != cpfValido[i]:
                return render(request, 'index.html',{
                    'pacientes': pacientes,
                    'retorno_salvar': 'O CPF é inválido'
                })
    
    paciente = Paciente.objects.get(id=id)
    paciente.nome = nome
    paciente.idade = idade
    paciente.sexo = sexo
    paciente.email = email
    paciente.telefone = telefone
    paciente.cpf = cpf
    
    paciente.data_de_nascimento = (data_de_nascimento).strftime("%Y-%m-%d")
    paciente.save()

    pacientes = Paciente.objects.all()
    return redirect(home)






## Condicao de Saude
@login_required(login_url="/core/autenticacao")
def home_condicao_de_saude(request, id_paciente): # Form e Read via Table de Condições de Saude
    condicoesDeSaude = CondicaoDeSaude.objects.all()
    paciente = Paciente.objects.get(id=id_paciente)
    return render(request, 'index_condicao_de_saude.html',{
        'condicoesDeSaude': condicoesDeSaude,
        'paciente': paciente})

@login_required(login_url="/core/autenticacao")
def salvar_condicao_de_saude(request, id_paciente):
    condicoesDeSaude = CondicaoDeSaude.objects.all()
    paciente = Paciente.objects.get(id=id_paciente)
    nome = request.POST.get("nome")
    descricao = request.POST.get("descricao")
    area = request.POST.get("area")
    gravidade = int(request.POST.get("gravidade"))
    idDoPaciente_id = int(request.POST.get("idDoPaciente_id"))
    
    if area not in ('Psicológico','Psiquiátrico','Endocrinológico','Nutricional','Neurológico','Físico'):
        return render(request, 'index_condicao_de_saude.html',{
            'condicoesDeSaude': condicoesDeSaude,
            'paciente': paciente,
            'retorno_salvar': 'As únicas áreas permitidas são: Psicológico, Psiquiátrico, Endocrinológico, Nutricional, Neurológico, Físico'
        })
    
    if gravidade > 10 or gravidade < 0:
        return render(request, 'index_condicao_de_saude.html',{
            'condicoesDeSaude': condicoesDeSaude,
            'paciente': paciente,
            'retorno_salvar': 'A gravidade não pode ser maior do que 10 nem menor do que 0'
        })

    CondicaoDeSaude.objects.create(nome=nome,
                            descricao=descricao,
                            area=area,
                            gravidade=gravidade,
                            idDoPaciente_id=idDoPaciente_id)
    
    condicoesDeSaude = CondicaoDeSaude.objects.all()
    return render(request, 'index_condicao_de_saude.html',{
        'condicoesDeSaude': condicoesDeSaude,
        'paciente': paciente,
        'retorno_salvar': 'Operação de criação bem-sucedida!'
    })

@login_required(login_url="/core/autenticacao")
def alterar_condicao_de_saude(request, id_paciente, id):
    condicaoDeSaude = CondicaoDeSaude.objects.get(id=id)
    paciente = Paciente.objects.get(id=id_paciente)
    return render(request, "alteracao_condicao_de_saude.html",{"condicaoDeSaude": condicaoDeSaude,"paciente":paciente})

@login_required(login_url="/core/autenticacao")
def excluir_condicao_de_saude(request, id_paciente, id):
    condicaoDeSaude = CondicaoDeSaude.objects.get(id=id)
    condicaoDeSaude.delete()
    return redirect(home_condicao_de_saude, id_paciente=id_paciente)

@login_required(login_url="/core/autenticacao")
def editar_condicao_de_saude(request, id_paciente, id):    
    condicoesDeSaude = CondicaoDeSaude.objects.all()
    paciente = Paciente.objects.get(id=id_paciente)
    
    nome = request.POST.get("nome")
    descricao = request.POST.get("descricao")
    area = request.POST.get("area")
    gravidade = int(request.POST.get("gravidade"))
    
    if area not in ('Psicológico','Psiquiátrico','Endocrinológico','Nutricional','Neurológico','Físico'):
        return render(request, 'index_condicao_de_saude.html',{
            'condicoesDeSaude': condicoesDeSaude,
            'paciente': paciente,
            'retorno_salvar': 'As únicas áreas permitidas são: Psicológico, Psiquiátrico, Endocrinológico, Nutricional, Neurológico, Físico'
        })
    
    if gravidade > 10 or gravidade < 0:
        return render(request, 'index_condicao_de_saude.html',{
            'condicoesDeSaude': condicoesDeSaude,
            'paciente': paciente,
            'retorno_salvar': 'A gravidade não pode ser maior do que 10 nem menor do que 0'
        })
    
    condicaoDeSaude = CondicaoDeSaude.objects.get(id=id)
    condicaoDeSaude.nome = nome
    condicaoDeSaude.descricao = descricao
    condicaoDeSaude.area = area
    condicaoDeSaude.gravidade = gravidade
    condicaoDeSaude.save()

    condicoesDeSaude = CondicaoDeSaude.objects.all()
    return redirect(home_condicao_de_saude, id_paciente=id_paciente)









## Psicologo
def autenticacao(request): ## Login do Psicologo
    if request.method == 'GET':
        return render(request, 'autenticacao.html')
    else:
        deslogar = request.POST.get('deslogar')
        if deslogar:
            logout(request)
            return render(request, 'autenticacao.html',{
                'logado': "Você foi deslogado com sucesso!"
            })
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')
        usuario = authenticate(username=nome,password=senha)
        if usuario is not None:
            login(request, usuario)
            return render(request, 'autenticacao.html',{
                'logado': "Você está autenticado no sistema!"
            })
        else:
            return render(request, 'autenticacao.html',{
                'logado': "Algo deu errado. Refaça os passos."
            })

def cadastro(request): ## Cadastro do Psicologo
    if request.method == 'GET':
        return render(request, 'cadastro.html')

    usuario, email, senha = request.POST.get('username'), request.POST.get('email'), request.POST.get('senha')
    user = User.objects.filter(username=usuario).first()
    if user:
        return render(request, 'cadastro.html',{
            'erro': 'Não foi possível criar pois o nome já existe'
        })
    
    user = User.objects.create_user(username=usuario, email=email, password=senha)
    user.save()

    return render(request, 'cadastro.html',{
            'erro': 'O usuário foi criado com sucesso!'
        })