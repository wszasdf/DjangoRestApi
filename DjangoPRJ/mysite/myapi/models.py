from django.db import models

# Create your models here.

# models.py
from django.db import models

class End_Report(models.Model):
    serialnumber = models.CharField(max_length=60)
    status = models.CharField(max_length=60)
    symptomlabel = models.CharField(max_length=60)
    location_id = models.CharField(max_length=60)

    # https://github.com/TheDumbfounds/django-rest-api-tutorial/blob/master/rest-tutorial-filtering/snippets/models.py
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.serialnumber

'''
class Hero(models.Model):
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)
    def __str__(self):
        return self.name
'''