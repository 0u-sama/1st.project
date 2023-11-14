from django.db import models


# Create your models here.


class Destination(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    image = models.ImageField(upload_to='pictures')
    price = models.IntegerField()

    """def __init__(self, name, desc, image, price):
        super().__init__(name=models.CharField(max_length=100), desc=models.TextField, image=models.ImageField,
                         price=models.IntegerField)
        self.name = name
        self.desc = desc
        self.img = image
        self.price = price"""
