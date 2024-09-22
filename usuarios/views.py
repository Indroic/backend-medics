from django.contrib.auth import authenticate

from rest_framework.decorators import  permission_classes
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated


from .models import Usuario
from .serializers import UsuarioSerializer


class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAdminUser]
    
class ChangeUserProfileViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticated]
    
    def list(self, request, *args, **kwargs):
        get_usuario = self.queryset.filter(id=self.request.user.id)
        serialize:UsuarioSerializer = self.get_serializer(get_usuario)
        return Response(serialize.data, status=200)
    
    def retrieve(self, request, *args, **kwargs):
        get_usuario = self.queryset.filter(id=self.request.user.id)
        serialize:UsuarioSerializer = self.get_serializer(get_usuario)
        return Response(serialize.data, status=200)
    
    def create(self, request, *args, **kwargs):
        return Response({"error": "Method not allowed"}, status=405)
    
    
    def destroy(self, request, *args, **kwargs):
        return Response({"error": "Method not allowed"}, status=405)
    
