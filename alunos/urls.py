from django.urls import path
from .views import listar_alunos, detalhar_aluno

app_name = 'alunos'

urlpatterns = [
    path('<str:id_aluno>/<slug_aluno>/', detalhar_aluno, name='detalhes_aluno'),
    path('<slug_materia>/', listar_alunos, name='listar_alunos_por_materia'),
    path('', listar_alunos, name='listar_alunos'),
]
