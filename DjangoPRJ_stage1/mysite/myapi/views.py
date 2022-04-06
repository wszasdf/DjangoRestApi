from django.shortcuts import render

# Create your views here.

# views.py
from rest_framework import viewsets

from .serializers import HeroSerializer
from .models import Hero


class HeroViewSet(viewsets.ModelViewSet):
    serializer_class = HeroSerializer
    queryset = Hero.objects.all().order_by('name')
    #queryset = Hero.objects.filter(id__icontains="3") # added 04/01/2022

    ### https://www.geeksforgeeks.org/filter-data-in-django-rest-framework/ __ ###
    filter_fields = (
        'id',
        'name',
        'alias',
    )
    ############################################################# added 04/01/2022