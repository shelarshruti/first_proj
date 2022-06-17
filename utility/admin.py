from django.contrib import admin
from utility.models import Products

# Register your models here.
@admin.register(Products)
class Products(admin.ModelAdmin):
    pass
