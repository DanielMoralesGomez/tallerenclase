from django.shortcuts import render
from rest_framework import viewsets,filters
from .models import Autor
from .serializer import AutorSerializer
from django_filters.rest_framework import DjangoFilterBackend

class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
    ]
    filterset_fields = ('__all__')
    search_fields = ('__all__')