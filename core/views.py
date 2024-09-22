from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.middleware.csrf import get_token

class CSRFAPIView(APIView):

    def get(self, request, format=None):
        csrf_token = get_token(request)
        return Response({'csrf_token': csrf_token})