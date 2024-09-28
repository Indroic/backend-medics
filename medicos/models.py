import uuid

from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.html import format_html
from django.urls import reverse

from usuarios.models import Usuario

from django_resized import ResizedImageField

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
    return "medicos-fotos/{0}".format(nuevo_nombre)


# Create your models here.
class Especialidad(models.Model):
    especialidad = models.CharField(max_length=100, unique=True, verbose_name="Especialidad")
    
    create_at = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name="Fecha de Creacion")
    
    update_at = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="Fecha de Actualizacion")
    
    class Meta:
        verbose_name = "Especialidad"
        verbose_name_plural = "Especialidades"
    
    def __str__(self):
        return self.especialidad

class Medico(models.Model):
    nombre = models.CharField(max_length=100, blank=False, null=False, unique=False, verbose_name="Primer Nombre")
    
    apellido = models.CharField(max_length=100, blank=False, null=False, unique=False, verbose_name="Primer Apellido")
    
    telefono = PhoneNumberField(blank=False, null=False, unique=False, verbose_name="Número de Teléfono")
    
    institucion = models.CharField(max_length=100, blank=False, null=False, unique=False, verbose_name="Institución")
    
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE, blank=False, null=False, unique=False, verbose_name="Especialidad")
    
    agregado_por = models.ForeignKey(Usuario, on_delete=models.CASCADE, blank=False, null=False, unique=False, verbose_name="Agregado Por")
    
    id = models.UUIDField(default=uuid.uuid4, null=False, blank=False, primary_key=True, verbose_name="ID")
    
    foto = ResizedImageField(upload_to=generar_nombre, null=True, blank=True, verbose_name="Foto de Medico", size=[736, 736],  crop=['middle', 'center'], db_column="medic_image")
    
    create_at = models.DateTimeField(auto_now=True, null=False, blank=False, verbose_name="Fecha de Creacion")
    
    update_at = models.DateTimeField(auto_now_add=True, null=False, blank=False, verbose_name="Fecha de Actualizacion")
    
    class Meta:
        verbose_name = "Medico"
        verbose_name_plural = "Medicos"
    
    def __str__(self):
        return self.nombre + " " + self.apellido + " - " + self.institucion + " - " + self.especialidad.especialidad
