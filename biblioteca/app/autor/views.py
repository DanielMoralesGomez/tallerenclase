from django.shortcuts import render
from rest_framework import viewsets
from .models import Autor
from .serializer import AutorSerializer

class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
