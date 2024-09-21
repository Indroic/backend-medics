from rest_framework import routers

from .views import UsuarioViewSet

router = routers.DefaultRouter()

router.register(r'users', UsuarioViewSet, basename='login')

urlpatterns = router.urls