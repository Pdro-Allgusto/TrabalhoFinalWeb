from django.contrib import admin
from .models import Professor, Materia


@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ['nome', 'idade', 'ra', 'email', 'imagem', 'slug', 'materia', 'criado', 'modificado', 'ativo']


@admin.register(Materia)
class MateriaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'slug']