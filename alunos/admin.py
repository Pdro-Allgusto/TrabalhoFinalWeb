from django.contrib import admin
from .models import Aluno, Materia


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'idade', 'ra', 'email', 'imagem', 'slug', 'materia', 'nota', 'criado', 'modificado', 'ativo']


@admin.register(Materia)
class MateriaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'slug']
