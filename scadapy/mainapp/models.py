from django.db import models


class Task(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField (max_length=250)
    start = models.DateTimeField()
    end = models.DateTimeField()
    progress = models.IntegerField()
    dependencies =  models.CharField(max_length=50)
    custom_class =  models.CharField(max_length=50)
