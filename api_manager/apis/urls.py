from django.urls import path
from .views import home, list_api_keys, generate_api_key

urlpatterns = [
    path("", home, name="home"),
     path("generate-key/", generate_api_key, name="generate-key"),
    path("list-keys/", list_api_keys, name="list-keys"),
]
