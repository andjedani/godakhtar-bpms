from django.db import models
from django.contrib.postgres.fields import ArrayField


class Feature(models.Model):
    name = models.CharField(max_length=255)
    values = ArrayField(models.CharField(max_length=127))


class Product(models.Model):
    pass
