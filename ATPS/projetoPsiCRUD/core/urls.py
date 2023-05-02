from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    ## Paciente
    path('', views.home, name="home"), # Form e Read via Table de Pacientes
    path('exportar_paciente', views.ListaPacientesPdfView.as_view(), name="exportar_paciente"), # Exportação PDF de Pacientes
    path('salvar_paciente', views.salvar_paciente, name="salvar_paciente"), # Form e Read de Pacientes
    path('alterar_paciente/<int:id>', views.alterar_paciente, name="alterar_paciente"), # Tela de Alteração de Pacientes
    path('editar_paciente/<int:id>', views.editar_paciente, name="editar_paciente"), # Edição de Pacientes(Reflete no Banco)
    path('excluir_paciente/<int:id>', views.excluir_paciente, name="excluir_paciente"), # Edição de Pacientes(Reflete no Banco)

    ## Condicao de Saude
    path('condicao_de_saude/<int:id_paciente>', views.home_condicao_de_saude, name="index_condicao_de_saude"), # Form e Read via Table de Condicoes de Saude
    path('condicao_de_saude/<int:id_paciente>/exportar_condicao_de_saude', views.ListaCondicoesDeSaudePdfView.as_view(), name="exportar_condicao_de_saude"), # Exportação PDF de Condicoes de Saude
    path('condicao_de_saude/<int:id_paciente>/salvar_condicao_de_saude', views.salvar_condicao_de_saude, name="salvar_condicao_de_saude"), # Form e Read de Condicoes de Saude
    path('condicao_de_saude/<int:id_paciente>/alterar_condicao_de_saude/<int:id>', views.alterar_condicao_de_saude, name="alterar_condicao_de_saude"), # Tela de Alteração de Condicoes de Saude
    path('condicao_de_saude/<int:id_paciente>/editar_condicao_de_saude/<int:id>', views.editar_condicao_de_saude, name="editar_condicao_de_saude"), # Edição de Condicoes de Saude(Reflete no Banco)
    path('condicao_de_saude/<int:id_paciente>/excluir_condicao_de_saude/<int:id>', views.excluir_condicao_de_saude, name="excluir_condicao_de_saude"), # Edição de Condicoes de Saude(Reflete no Banco)

    ## Psicologo
    path('cadastro', views.cadastro, name="cadastro"), ## Cadastro do Psicologo
    path('autenticacao', views.autenticacao, name="autenticacao")  ## Login do Psicologo
]