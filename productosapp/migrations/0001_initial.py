# Generated by Django 4.2.1 on 2023-05-27 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=300)),
                ('price', models.FloatField()),
                ('img', models.ImageField(upload_to='')),
                ('category', models.CharField(choices=[('Acc', 'Accion'), ('Adv', 'Aventura'), ('Arc', 'Arcade'), ('Dep', 'Deportes'), ('Est', 'Estrategia'), ('Sim', 'Simulacion'), ('Gad', 'Aventura Grafica'), ('Rol', 'Rol'), ('Mus', 'Musical'), ('Box', 'Sandbox')], max_length=20)),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Producto',
            },
        ),
    ]
