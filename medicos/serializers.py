from rest_framework import serializers
from .models import Medico, Especialidad

from usuarios.serializers import GeneroSerializer


class EspecialidadSerializer(serializers.ModelSerializer):
    genero = GeneroSerializer()
    class Meta:
        model = Especialidad
        fields = '__all__'


class MedicoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Medico
        fields = '__all__'
        
class MedicoListSerializer(serializers.ModelSerializer):
    especialidad = EspecialidadSerializer()
    class Meta:
        model = Medico
        fields = '__all__'