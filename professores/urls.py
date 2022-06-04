from django.urls import path
from .views import listar_professores, detalhar_professor

app_name = 'professores'

urlpatterns = [
    path('<str:id_professor>/<slug_professor>/', detalhar_professor, name='detalhes_professor'),
    path('<slug_materia>/', listar_professores, name='listar_professores_por_materia'),
    path('', listar_professores, name='listar_professores'),
]
