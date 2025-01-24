from django.db import models

# Create your models here.
#samochod
#wypozyczenie
#stan - sprzatniecy, opony, czysty
#klient
#

class Car(models.Model):
    id = models.IntegerField(primary_key=True)
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    hp = models.IntegerField()

class Rental(models.Model):
    car = models.ForeignKey(Car, null=True, blank=True, on_delete=models.RESTRICT)
    untill = models.DateField()


