# Generated by Django 3.2.7 on 2021-10-26 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('generales', '0002_auto_20211025_1946'),
    ]

    operations = [
        migrations.CreateModel(
            name='claseModelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activo', models.BooleanField(default=True)),
                ('creado', models.DateField(auto_now_add=True)),
                ('modificado', models.DateField(auto_now=True)),
            ],
        ),
    ]
