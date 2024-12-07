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

class Stock(models.Model):
    Addr = models.CharField(max_length=20)
    Staff_id = models.ForeignKey("Staff",on_delete=models.DO_NOTHING)
    Capacity = models.IntegerField()
    CarStock = models.ManyToManyField(Car,through='Car_Stock')

class Car_Stock(models.Model):
    Car_id = models.ForeignKey("Car",on_delete=models.DO_NOTHING)
    Stock_id = models.ForeignKey("Stock",on_delete=models.DO_NOTHING)
    Num = models.IntegerField()

class Staff(models.Model):
    Name = models.CharField(max_length=20)
    Sex = models.CharField(max_length=20)
    Age = models.IntegerField()
    Phone = models.CharField(max_length=20)
    Native_Addr = models.CharField(max_length=20)
    Salary = models.FloatField()
    Position = models.CharField(max_length=20)
    