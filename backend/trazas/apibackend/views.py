from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets

from .serializers import FrezHhzTc9920200321Serializer
from .models import FrezHhzTc9920200321


class TrazaViewSet(viewsets.ModelViewSet):
    # queryset = FrezHhzTc9920200321.objects.all().order_by('st')
    queryset = FrezHhzTc9920200321.objects.all().order_by('st')[:10]
    serializer_class = FrezHhzTc9920200321Serializer