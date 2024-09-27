# Generated by Django 5.1.1 on 2024-09-26 19:54

import django_resized.forms
import usuarios.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0010_alter_usuario_avatar_alter_usuario_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='avatar',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], db_column='profile_image', force_format=None, keep_meta=True, null=True, quality=-1, scale=None, size=[736, 736], upload_to=usuarios.models.generar_nombre, verbose_name='Avatar'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.EmailField(blank=True, default='no-email.61bf03a9ad9b4362b3a02197f708e7c0@noemail.com', max_length=254, null=True, unique=True, verbose_name='Correo Electronico'),
        ),
    ]