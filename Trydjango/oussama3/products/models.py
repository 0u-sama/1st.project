from django.db import models


# Create your models here.

class Product(models.Model):
    title = models.CharField(blank=False, max_length=100)
    description = models.TextField(blank=False, null=True)
    price = models.DecimalField(blank=False, decimal_places=2, max_digits=10000)
    summary = models.TextField(blank=True)
    available = models.BooleanField(default=True, null=False)
