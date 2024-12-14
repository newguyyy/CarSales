from django.db import models
from Basic.models import Car

# Create your models here.
class Supplier(models.Model):
    Name = models.CharField(max_length=20)
    Phone = models.CharField(max_length=20)
    Addr = models.CharField(max_length=20)
    Car_id = models.ManyToManyField(Car,through='Car_Supplier')

class Car_Supplier(models.Model):
    Car_id = models.ForeignKey(Car,on_delete=models.DO_NOTHING)
    Num = models.IntegerField()
    Supplier_id = models.ForeignKey(Supplier,on_delete=models.DO_NOTHING)
    Date = models.DateField()
    TotalPrice = models.FloatField()

