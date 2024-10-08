# Generated by Django 5.1 on 2024-08-31 18:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('autor', '0001_initial'),
        ('genero', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=300)),
                ('fecha_publicacion', models.DateField()),
                ('disponible', models.BooleanField(default=True)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autor.autor')),
                ('genero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='genero.genero')),
            ],
        ),
    ]
