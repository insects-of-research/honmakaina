from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, filters

from .models import Word2Vec
from .serializer import Word2VecSerializer


class Word2VecViewSet(viewsets.ModelViewSet):
    queryset = Word2Vec.objects.all()
    serializer_class = Word2VecSerializer

