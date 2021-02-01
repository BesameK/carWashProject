from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class Washer(models.Model):
    first_name=models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    percent=models.PositiveSmallIntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)],verbose_name='Percent from price')

    def __str__(self):
        return f"{self.last_name}  {self.first_name} : percent {self.percent}"
    class Meta:
        verbose_name = 'Washer'
        verbose_name_plural = 'Washers'



class Car(models.Model):

    carType=models.CharField(max_length=16,verbose_name="Car Make")
    carModel=models.CharField(max_length=16,verbose_name="Car Model")
    carYear =models.PositiveSmallIntegerField(validators=[MinValueValidator(1886),MaxValueValidator(2021)],verbose_name="Car Model Year")

    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'

    def __str__(self):
        return f'{self.carType} {self.carModel}'



class Order(models.Model):
    order_date=models.DateTimeField(verbose_name="Order Date/Time")
    end_date=models.DateTimeField(verbose_name="End Date/Time")
    price=models.IntegerField(verbose_name='price')
    washer=models.ForeignKey('car_wash.Washer',on_delete=models.PROTECT)
    car=models.ForeignKey('car_wash.Car',on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.washer.last_name} : {self.car.carModel}'

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'



