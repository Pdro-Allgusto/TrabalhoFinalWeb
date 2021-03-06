# Generated by Django 3.2.9 on 2021-11-30 04:25

from django.db import migrations, models
import django.db.models.deletion
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Data de Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Data de Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('nome', models.CharField(db_index=True, max_length=100)),
                ('slug', models.SlugField(blank=True, editable=False, max_length=250, unique=True, verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'materia',
                'verbose_name_plural': 'materias',
                'ordering': ('nome',),
            },
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Data de Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Data de Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('nome', models.CharField(max_length=200, verbose_name='Nome')),
                ('idade', models.IntegerField(verbose_name='Idade')),
                ('ra', models.CharField(max_length=8, verbose_name='Registro Academico')),
                ('email', models.CharField(max_length=200, verbose_name='Email')),
                ('imagem', stdimage.models.StdImageField(upload_to='professores', verbose_name='Imagem')),
                ('slug', models.SlugField(blank=True, editable=False, max_length=250, unique=True, verbose_name='Slug')),
                ('materia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='professores.materia', verbose_name='Materia')),
            ],
            options={
                'verbose_name': 'professor',
                'verbose_name_plural': 'professores',
                'ordering': ('nome',),
            },
        ),
    ]
