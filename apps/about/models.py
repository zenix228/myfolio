from django.db import models

class About(models.Model):
    name = models.CharField(max_length=250)
    data =  models.IntegerField()
    about = models.CharField(max_length=100)
    