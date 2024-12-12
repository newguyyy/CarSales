from django.db import models

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
    InputPrice = models.FloatField()
    OutputPrice = models.FloatField()

class Staff(models.Model):
    Name = models.CharField(max_length=20)
    Sex = models.CharField(max_length=20)
    Age = models.IntegerField()
    Phone = models.CharField(max_length=20)
    Native_Addr = models.CharField(max_length=20)
    Salary = models.FloatField()
    Position = models.CharField(max_length=20)