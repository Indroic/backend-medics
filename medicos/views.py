from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.request import Request

from .serializers import MedicoSerializer, EspecialidadSerializer, MedicoListSerializer
from .models import Medico, Especialidad


class MedicoViewSet(ModelViewSet):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer
    permission_classes = [IsAuthenticated]
    
    
    def list(self, request, *args, **kwargs):
        medicos = Medico.objects.all().filter(agregado_por=self.request.user)
        
        return Response({"medicos": MedicoListSerializer(medicos, many=True).data})
    
    def create(self, request: Request, *args, **kwargs):
        request.data["agregado_por"] = self.request.user.id

        return super().create(request, *args, **kwargs)
    def partial_update(self, request: Request, *args, **kwargs):
        medico = Medico.objects.get(id=super().partial_update(request, *args, **kwargs).data["id"])
        

        return Response(data=MedicoListSerializer(medico).data)

class EspecialidadViewSet(ModelViewSet):
    queryset = Especialidad.objects.all()
    serializer_class = EspecialidadSerializer
