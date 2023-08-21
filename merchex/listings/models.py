from django.db import models

class Band(models.Model) :
    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField()
    biography = models.fields.CharField()
    year_formed = models.fields.IntegerField()
    active = models.fields.BooleanField()
    official_homepage = models.fields.URLField()
