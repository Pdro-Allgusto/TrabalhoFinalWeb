# Generated by Django 3.2.9 on 2021-11-30 04:15

from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='imagem',
            field=stdimage.models.StdImageField(upload_to='alunos', verbose_name='Imagem'),
        ),
    ]