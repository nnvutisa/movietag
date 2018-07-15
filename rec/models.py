from __future__ import unicode_literals

from django.db import models

# Create your models here.

class MovieRec(models.Model):
    movie_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    rec1 = models.CharField(max_length=200)
    rec2 = models.CharField(max_length=200)
    rec3 = models.CharField(max_length=200)
    rec4 = models.CharField(max_length=200)
    rec5 = models.CharField(max_length=200)
    rec6 = models.CharField(max_length=200)
    rec7 = models.CharField(max_length=200)
    rec8 = models.CharField(max_length=200)
    rec9 = models.CharField(max_length=200)
    rec10 = models.CharField(max_length=200)

    def __str__(self):
        return self.name
