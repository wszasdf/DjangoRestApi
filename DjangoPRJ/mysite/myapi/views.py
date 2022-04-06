from django.shortcuts import render

# Create your views here.

# views.py
from rest_framework import viewsets

from .serializers import End_ReportSerializer
from .models import End_Report

#### https://www.geeksforgeeks.org/filter-data-in-django-rest-framework/ ####
from django_filters import  rest_framework as filters

#### https://github.com/TheDumbfounds/django-rest-api-tutorial/blob/master/rest-tutorial-filtering/snippets/api/viewsets.py ####
from rest_framework.decorators import action
from rest_framework.response import Response

class End_ReportFilter(filters.FilterSet):
    id = filters.CharFilter(lookup_expr='icontains') # added 04/06/2022
    serialnumber = filters.CharFilter(lookup_expr='icontains')
    status = filters.CharFilter(lookup_expr='icontains') # added 04/06/2022
    symptomlabel = filters.CharFilter(lookup_expr='icontains') # added 04/06/2022
    location_id = filters.CharFilter(lookup_expr='icontains') # added 04/06/2022
    #time = filters.CharFilter(lookup_expr='icontains') # added 04/06/2022

    class Meta:
        model = End_Report
        exclude = ('active')
        filter_fields = {'id': ['icontains'], # added 04/06/2022
                         'serialnumber': ['icontains'],
                         'status': ['icontains'], # added 04/06/2022
                         'symptomlabel': ['icontains'], # added 04/06/2022
                         'location_id': ['icontains'], # added 04/06/2022
                         'time': ['iexact', 'lte', 'gte'] # added 04/06/2022
        }
#############################################################################

class End_ReportViewSet(viewsets.ModelViewSet):

    serializer_class = End_ReportSerializer
    queryset = End_Report.objects.all()#.order_by('serialnumber')
    #queryset = Hero.objects.filter(id__icontains="3") # added 04/01/2022
    filterset_class = End_ReportFilter


    #### https://github.com/TheDumbfounds/django-rest-api-tutorial/blob/master/rest-tutorial-filtering/snippets/api/viewsets.py ####
    @action(methods=['get'], detail=False)
    def newest(self, request):
        newest = self.get_queryset().order_by('time').last()
        serializer = self.get_serializer_class()(newest)
        return Response(serializer.data)
    ################################################################################################################################

    #### https://www.geeksforgeeks.org/filter-data-in-django-rest-framework/ ####
    '''filter_fields = (
        'id',
        'serialnumber',
        'status',
        'symptomlabel',
        'location_id',
        'time'
    )'''
    #############################################################################

    #### https://www.youtube.com/watch?v=s9V9F9Jtj7Q&t=119s ####
    '''def get_queryset(self):
        return End_Report.objects.filter(serialnumber__icontains='FWI2205-00659')'''
    ############################################################