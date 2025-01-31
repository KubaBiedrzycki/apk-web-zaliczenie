from django.contrib import admin

# Register your models here.

from .models import Car, Rental, Client, Condition

#class CarAdmin(admin.ModelAdmin):
    #list_display = ['brand', 'model']

admin.site.register(Car)
admin.site.register(Client)
admin.site.register(Rental)
admin.site.register(Condition)