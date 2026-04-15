from django.db import models

# Create your models here.
class FruitModel(models.Model):
    name = models.CharField(max_length=25)
    price = models.IntegerField(default=50)

# name price
# apple 50
# adcv 50
# mango 27