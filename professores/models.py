from django.db import models
from stdimage.models import StdImageField
from django.db.models import signals
from django.template.defaultfilters import slugify
from django.urls import reverse

class Base(models.Model):

    criado = models.DateField('Data de Criação', auto_now_add=True)
    modificado = models.DateField('Data de Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo', default=True)

    class Meta:
        abstract = True

class Materia(Base):

    nome = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField('Slug', max_length=250, unique=True, blank=True, editable=False)

    class Meta:
        ordering = ('nome',)
        verbose_name = 'materia'
        verbose_name_plural = 'materias'

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse(
            'professores:listar_professores_por_materia',
            kwargs={
                'slug_materia': self.slug
            }
        )


class Professor(Base):
    nome = models.CharField('Nome', max_length=200)
    idade = models.IntegerField('Idade')
    ra = models.CharField('Registro Academico', max_length=8)
    email = models.CharField('Email', max_length=200)
    imagem = StdImageField('Imagem', upload_to='professores', variations={'thumb': (300, 300)})
    slug = models.SlugField('Slug', max_length=250, unique=True, blank=True, editable=False)
    materia = models.ForeignKey('professores.Materia', verbose_name='Materia', on_delete=models.CASCADE)

    class Meta:
        ordering = ('nome',)
        verbose_name = 'professor'
        verbose_name_plural = 'professores'

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse(
            'professores:detalhes_professor',
            kwargs={
                'id_professor': self.id,
                'slug_professor': self.slug
            }
        )


def professor_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.nome)

def materia_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.nome)

signals.pre_save.connect(professor_pre_save, sender=Professor)
signals.pre_save.connect(materia_pre_save, sender=Materia)
