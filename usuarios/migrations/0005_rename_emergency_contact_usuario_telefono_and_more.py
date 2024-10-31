# Generated by Django 5.1.1 on 2024-10-31 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_alter_usuario_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='emergency_contact',
            new_name='telefono',
        ),
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.EmailField(blank=True, default='no-email.a6c8986f0e4944b1ac4dca3de0c2bfdf@noemail.com', max_length=254, null=True, unique=True, verbose_name='Correo Electrónico'),
        ),
    ]
