from django.db import models

class Album(models.Model):
    artist = models.CharField(max_length=75)
    name = models.CharField(max_length=100)
    release = models.DateField()
    order = models.IntegerField(blank=True, null=True)