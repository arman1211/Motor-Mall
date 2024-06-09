from django.db import models
from brand.models import BrandModel
from django.contrib.auth.models import User

# Create your models here.

class CarModel(models.Model):
    name = models.CharField(max_length=50)
    image=models.ImageField( upload_to='car/media/cars/')
    description = models.TextField()
    quantity = models.PositiveSmallIntegerField()
    price = models.IntegerField()
    brand = models.ForeignKey(BrandModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Purchase(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    car = models.ForeignKey(CarModel,on_delete=models.CASCADE)