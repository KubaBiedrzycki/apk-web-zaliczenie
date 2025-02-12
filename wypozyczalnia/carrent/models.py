from django.db import models


class Condition(models.Model):
    cleanIn = models.BooleanField(default=True)
    cleanOut = models.BooleanField(default=True)
    tires = models.CharField(max_length=50)

    def clean_in_text(self):
        return "Czyste wew." if self.cleanIn else "Brudne wew."

    def clean_out_text(self):
        return "Czyste zew." if self.cleanOut else "Brudne zew."
    
    def __str__(self):
        return f"{self.clean_in_text()} {self.clean_out_text()} {self.tires}"

class Client(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    age = models.IntegerField()
    drivingLicense = models.BooleanField(default=True)
    drivingLicenseUntill = models.DateField()

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

    class Meta:
        ordering = ['firstname', 'lastname']
    
class Car(models.Model):
    id = models.IntegerField(primary_key=True)
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    hp = models.IntegerField()
    drive = models.CharField(max_length=50)
    condition = models.ForeignKey(Condition, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.brand} {self.model} {self.color} {self.hp}"
    
    class Meta:
        ordering = ['id', 'brand']

class Rental(models.Model):
    car = models.ForeignKey(Car, null=True, blank=True, on_delete=models.RESTRICT)
    untill = models.DateField()
    client = models.ForeignKey(Client, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.car} {self.untill} {self.client}"
