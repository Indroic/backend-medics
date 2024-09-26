import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django_resized import ResizedImageField
from django.urls import reverse
from django.utils.html import format_html

def generar_nombre(instance, filename):
    """
    Genera un nombre unico para el archivo y lo retorna
    """


    # obtiene la extension del archivo
    extension = filename.split('.')[-1]
    # obtiene el nombre del usuario
    usuario = instance.username
    
    # genera una cadena de caracteres para el nombre del archivo y elimina todos los "-" que tenga
    caracteres = str(uuid.uuid4()).replace('-', '')
    # crea el nuevo nombre
    nuevo_nombre = usuario + "." + caracteres + "." + extension
    # retorna el nuevo nombre
    return "avatars/{0}".format(nuevo_nombre)

def generar_strings():
    return "no-content."+(str(uuid.uuid4()).replace('-', ''))

class Usuario(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, blank=False, null=False)
    
    ci = models.IntegerField(unique=True, blank=True, null=True, verbose_name="Cédula de Identidad")
    
    first_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Primer Nombre")
    
    last_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Primer Apellido")
    
    email = models.EmailField(blank=True, null=True, verbose_name="Correo Electronico", unique=True, default=f"no-email.{str(uuid.uuid4()).replace('-', '')}@noemail.com")
    
    create_at = models.DateTimeField(auto_now=True, null=False, blank=False, verbose_name="Fecha de Creacion")
    
    update_at = models.DateTimeField(auto_now_add=True, null=False, blank=False, verbose_name="Fecha de Actualizacion")
    
    avatar = ResizedImageField(upload_to=generar_nombre, null=True, blank=True, verbose_name="Avatar", size=[736, 736],  crop=['middle', 'center'], db_column="profile_image", default="https://rnkqnkvcketqhptlupct.supabase.co/storage/v1/object/public/storage-medics/avatars/avatar-placeholder.png")
    


