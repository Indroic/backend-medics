from rest_framework import routers

from .views import UsuarioViewSet, ChangeUserProfileViewSet

router = routers.DefaultRouter()

router.register(r'users', UsuarioViewSet, basename='users')
router.register(r'profile', ChangeUserProfileViewSet, basename='profile')

urlpatterns = router.urls