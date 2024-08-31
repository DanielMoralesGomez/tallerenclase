

from django.shortcuts import render
from .models import Libro
from rest_framework import viewsets, filters
from .serializer import LibroSerializer
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

class LibroViewSet(viewsets.ModelViewSet):
    serializer_class = LibroSerializer
    queryset = Libro.objects.all()

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
    ]
    filterset_fields = ('__all__')
    search_fields = ('__all__')
