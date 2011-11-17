from django.db import models


# Create your models here.
class Api(models.Model):
    name = models.TextField(max_length=30)
    key = models.TextField(max_length=100)
    secret = models.TextField(max_length=100)
