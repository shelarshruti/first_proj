from django.contrib import admin
from relations.models import Album, Song, Author, Book, Vehicle, Car


# Register your models here.

@admin.register(Vehicle)
class Vehicle(admin.ModelAdmin):
    pass


@admin.register(Car)
class Car(admin.ModelAdmin):
    pass
