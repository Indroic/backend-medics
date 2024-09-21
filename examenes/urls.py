from rest_framework.routers import DefaultRouter

from .views import ExamenViewSet

router = DefaultRouter()

router.register(r'examenes', ExamenViewSet, basename='medicos')

urlpatterns = router.urls