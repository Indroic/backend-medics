from rest_framework.routers import DefaultRouter
from django.urls import path

from .views import MedicoViewSet, EspecialidadViewSet

router = DefaultRouter()

router.register(r'medicos', MedicoViewSet, basename='medicos')
router.register(r'especialidades', EspecialidadViewSet, basename='especialidades')

urlpatterns = router.urls

