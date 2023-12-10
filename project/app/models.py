from django.db import models

# Create your models here.
class CarBrand(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
class Car(models.Model):
    car_name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    carbrand = models.ForeignKey(CarBrand, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.car_name