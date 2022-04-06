# serializers.py
from rest_framework import serializers

from .models import End_Report

class End_ReportSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = End_Report
        fields = ('id', 'serialnumber', 'status', 'symptomlabel', 'location_id', 'time')