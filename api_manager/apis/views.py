from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .models import APIKey
from django.http import JsonResponse
import uuid




def home(request):
    return JsonResponse({"message": "Welcome to the API Manager!"})


def generate_api_key(request):
    new_key = APIKey.objects.create(key=str(uuid.uuid4()))
    return JsonResponse({"api_key": new_key.key})

def list_api_keys(request):
    keys = APIKey.objects.all().values("key", "created_at")
    return JsonResponse({"api_keys": list(keys)})


def delete_api_key(request, key):
    try:
        api_key = APIKey.objects.get(key=key)
        api_key.delete()
        return JsonResponse({"message": "API Key deleted successfully"})
    except APIKey.DoesNotExist:
        return JsonResponse({"error": "API Key not found"}, status=404)

class GenerateAPIKey(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        api_key = APIKey.objects.create(user=request.user)
        return Response({"api_key": api_key.key}, status=201)

class ListAPIKeys(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        keys = APIKey.objects.filter(user=request.user)
        return Response({"keys": [key.key for key in keys]})

class DeleteAPIKey(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, key):
        APIKey.objects.filter(user=request.user, key=key).delete()
        return Response({"message": "API Key deleted"}, status=200)
