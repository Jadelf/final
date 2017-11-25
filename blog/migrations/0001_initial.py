# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asignacion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('nombre', models.CharField(max_length=80)),
                ('precio', models.CharField(max_length=10)),
                ('empleado', models.CharField(max_length=80)),
                ('cliente', models.CharField(max_length=80)),
                ('register_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Plato',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AddField(
            model_name='menu',
            name='platos',
            field=models.ManyToManyField(through='blog.Asignacion', to='blog.Plato'),
        ),
        migrations.AddField(
            model_name='asignacion',
            name='menu',
            field=models.ForeignKey(to='blog.Menu'),
        ),
        migrations.AddField(
            model_name='asignacion',
            name='plato',
            field=models.ForeignKey(to='blog.Plato'),
        ),
    ]
