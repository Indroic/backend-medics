from django.middleware.csrf import get_token
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def get_csrf(request):
    return {"csrf_token": get_token(request)}