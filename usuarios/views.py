from django.contrib.auth import authenticate

from rest_framework.decorators import  permission_classes
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser


from .models import Usuario
from .serializers import UsuarioSerializer


class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAdminUser]