from django.urls import path
from . import views

urlappterns = [
    path('', views.api_home),
]