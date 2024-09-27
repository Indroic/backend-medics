from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import ExamenSerializer, CategoriaSerializer
from .models import Examen, Categoria

class ExamenViewSet(ModelViewSet):
    queryset = Examen.objects.all()
    serializer_class = ExamenSerializer
    permission_classes = [IsAuthenticated]
    
    def list(self, request, *args, **kwargs):
        examenes = Examen.objects.all().filter(agregado_por=self.request.user)
        
        return Response({"examenes": ExamenSerializer(examenes, many=True).data})
    
    def create(self, request, *args, **kwargs):
        data = request.data
        data["agregado_por"] = self.request.user.id
        data_serialize = ExamenSerializer(data=data)
        
        if data_serialize.is_valid():
            data_serialize.save()
            
            return Response(data_serialize.data, status=201)
        
        return Response(data_serialize.errors, status=400)
    
class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
