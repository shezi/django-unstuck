from django.db import models


class Demonstration(models.Model):

    name = models.CharField(max_length=128)
    index = models.IntegerField(default=0)
    value = models.FloatField()

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
