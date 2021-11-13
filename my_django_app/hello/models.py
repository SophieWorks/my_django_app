from django.db import models

# Create your models here.

from django.db import models

class scholarships(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

class getSchols(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)