# Generated by Django 2.1.8 on 2019-07-01 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_auto_20190701_1303'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfil',
            name='IdTipoDocu',
        ),
    ]
