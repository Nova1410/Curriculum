# Generated by Django 2.1.8 on 2019-06-25 23:26

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50, verbose_name='Correo electrónico')),
                ('asunto', models.CharField(default='Asunto', max_length=50, verbose_name='Asunto')),
                ('msj', ckeditor.fields.RichTextField(default='Quisiera', max_length=50, verbose_name='Mensaje')),
            ],
            options={
                'verbose_name': 'Mensaje contacto',
                'verbose_name_plural': 'Mensajes de contactos',
            },
        ),
    ]
