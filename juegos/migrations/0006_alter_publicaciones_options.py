# Generated by Django 4.2.1 on 2023-06-04 21:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('juegos', '0005_alter_perfil_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='publicaciones',
            options={'ordering': ['-timestamp']},
        ),
    ]
