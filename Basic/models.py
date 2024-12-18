from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator

# Create your models here.
class Car(models.Model):
    Color_Choice = [
        ('Red', 'Red'),
        ('Blue', 'Blue'),
        ('Black', 'Black'),
        ('White', 'White'),
        ('Yellow', 'Yellow'),
        ('Green', 'Green'),
    ]
    Color = models.CharField(max_length=20,choices=Color_Choice)
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200,null=True)
    InputPrice = models.FloatField()
    OutputPrice = models.FloatField()

class Staff(models.Model):
    Sex = models.CharField(max_length=20)
    Age = models.IntegerField()
    Phone = models.CharField(max_length=20)
    Native_Addr = models.CharField(max_length=20)
    Salary = models.FloatField(validators=[MinValueValidator(3000)])
    Position = models.CharField(max_length=20)
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)