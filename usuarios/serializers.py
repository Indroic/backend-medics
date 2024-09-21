from rest_framework import serializers
from .models import Usuario


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        exclude = [
            "is_superuser",
            "is_staff",
            "is_active",
            "last_login",
            "date_joined",
            "password",
        ]

