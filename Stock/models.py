from django.db import models
from Basic.models import Car,Staff



class Stock(models.Model):
    Addr = models.CharField(max_length=20)
    Staff_id = models.ForeignKey(Staff,on_delete=models.DO_NOTHING)
    Capacity = models.IntegerField()
    CarStock = models.ManyToManyField(Car,through='Car_Stock')

class Car_Stock(models.Model):
    Car_id = models.ForeignKey(Car,on_delete=models.DO_NOTHING)
    Stock_id = models.ForeignKey(Stock,on_delete=models.DO_NOTHING)
    Num = models.IntegerField()
