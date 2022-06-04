from django.shortcuts import render, get_object_or_404
from .models import Professor, Materia

def listar_professores(request, slug_materia=None):
    materia = None
    lista_materias = Materia.objects.all()
    lista_professores = Professor.objects.filter(ativo=True)
    if slug_materia:
        materia = get_object_or_404(Materia, slug=slug_materia)
        lista_professores = Professor.objects.filter(materia=materia)
    contexto = {
        'materia': materia,
        'lista_materias': lista_materias,
        'lista_professores': lista_professores,
    }
    return render(request, 'professores/professores.html', contexto)

def detalhar_professor(request, id_professor, slug_professor):

    professor = get_object_or_404(Professor,
                                id=id_professor,
                                slug=slug_professor,
                                ativo=True)
    contexto = {
        'professor': professor,
    }
    return render(request, 'professores/detalhes.html', contexto)

