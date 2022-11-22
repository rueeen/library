# Generated by Django 4.1.1 on 2022-11-21 20:18

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('name', models.CharField(max_length=200, primary_key=True, serialize=False, verbose_name='Nombre autor')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID Categoría')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre Categoría')),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID pais')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre pais')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('isbn', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='Isbn')),
                ('title', models.CharField(max_length=50, verbose_name='Título')),
                ('year', models.DateField(verbose_name='Año publicacion')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Descripción')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.author', verbose_name='Autor')),
                ('category', models.ManyToManyField(to='core.category', verbose_name='Categorias')),
            ],
        ),
        migrations.AddField(
            model_name='author',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.country', verbose_name='Pais autor'),
        ),
    ]
