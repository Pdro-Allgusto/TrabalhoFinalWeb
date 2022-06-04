from django.shortcuts import render, get_object_or_404
from .models import Aluno, Materia

def listar_alunos(request, slug_materia=None):
    materia = None
    lista_materias = Materia.objects.all()
    lista_alunos = Aluno.objects.filter(ativo=True)
    if slug_materia:
        materia = get_object_or_404(Materia, slug=slug_materia)
        lista_alunos = Aluno.objects.filter(materia=materia)
    contexto = {
        'materia': materia,
        'lista_materias': lista_materias,
        'lista_alunos': lista_alunos,
    }
    return render(request, 'alunos/alunos.html', contexto)

def detalhar_aluno(request, id_aluno, slug_aluno):

    aluno = get_object_or_404(Aluno,
                                id=id_aluno,
                                slug=slug_aluno,
                                ativo=True)
    contexto = {
        'aluno': aluno,
    }
    return render(request, 'alunos/detalhes.html', contexto)
