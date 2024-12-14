from django.db import models
from Basic.models import Car,Staff

# Create your models here.
class Client(models.Model):
    Work_Status_Chioce = [
        (0, 'unfinished'),
        (1, 'finished'),
    ]
    Name = models.CharField(max_length=20)
    Phone = models.CharField(max_length=20)
    Addr = models.CharField(max_length=20)
    Work_Status = models.IntegerField(choices=Work_Status_Chioce)
    Car_id = models.ManyToManyField(Car,through='Order')

class Order(models.Model):
    Car_id = models.ForeignKey(Car,on_delete=models.DO_NOTHING)
    Client_id = models.ForeignKey(Client,on_delete=models.DO_NOTHING)
    Staff_id = models.ForeignKey(Staff,on_delete=models.DO_NOTHING)
    Date = models.DateField()
    Total_Price = models.FloatField()
