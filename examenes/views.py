from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import ExamenSerializer, CategoriaSerializer, ExamenListSerializer
from .models import Examen, Categoria


class ExamenViewSet(ModelViewSet):
    queryset = Examen.objects.all()
    serializer_class = ExamenSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        examenes = Examen.objects.all().filter(agregado_por=self.request.user)

        return Response({"examenes": ExamenListSerializer(examenes, many=True).data})

    def create(self, request, *args, **kwargs):
        request.data["agregado_por"] = self.request.user.id
        medico = Examen.objects.get(
            id=super().create(request, *args, **kwargs).data["id"]
        )

        return Response(data=ExamenListSerializer(medico).data)

    def partial_update(self, request, *args, **kwargs):
        medico = Examen.objects.get(
            id=super().partial_update(request, *args, **kwargs).data["id"]
        )

        return Response(data=ExamenListSerializer(medico).data)


class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
