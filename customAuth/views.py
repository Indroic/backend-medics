from django.contrib.auth import authenticate

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAdminUser
from rest_framework.authentication import TokenAuthentication


from usuarios.models import Usuario
from usuarios.serializers import UsuarioSerializer

from .serializers import LoginSerializer


# Create your views here.

@api_view(["POST"])
def login(request,  *args, **kwargs):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid() is False:
        return Response(serializer.errors, status=400)
    print(serializer.validated_data)
    authenticated_user = authenticate(
        username=serializer.validated_data["username"],
        password=serializer.validated_data["password"],
    )
    if authenticated_user is None:
        print(authenticated_user)
        return Response({"error": "Invalid credentials"}, status=400)
    token, create = Token.objects.get_or_create(user=authenticated_user)
    return Response(
        {"token": token.key, "user": UsuarioSerializer(authenticated_user).data},
        status=200,
    )
    
@api_view(["POST"])
def register(request, *args, **kwargs):
    serializer = UsuarioSerializer(data=request.data)
    
    if serializer.is_valid() is False:
        return Response(serializer.errors, status=400)
    
    user = Usuario.objects.create_user(
        username=serializer.validated_data["username"],
        password=serializer.validated_data["password"],
        first_name=serializer.validated_data["first_name"],
        last_name=serializer.validated_data["last_name"],
        email=serializer.validated_data["email"],
        ci=serializer.validated_data["ci"],
    )
    
    serializer = UsuarioSerializer(user)
    
    return Response(serializer.data, status=201)
    
    