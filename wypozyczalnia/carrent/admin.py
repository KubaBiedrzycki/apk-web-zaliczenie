from django.contrib import admin

# Register your models here.

from .models import Car, Rental

#class CarAdmin(admin.ModelAdmin):
    #list_display = ['brand', 'model']

admin.site.register(Car)
admin.site.register(Rental)