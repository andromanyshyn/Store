from django.contrib import admin

from .models import *


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['name']
    fields = ['name', 'description']


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
    fields = ['name', 'description', 'price', 'image', 'category_id']


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ['__str__']
