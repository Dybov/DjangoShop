# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Category, Product

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name', 'category_slug']
    prepopulated_fields = {'category_slug': ('category_name',)}
class ProductAdmin(admin.ModelAdmin):
	list_display = ['name','slug', 'category', 'price', 'available', 'stock']
	list_filter = ['available', 'category',]
	list_editable = ['stock', 'available', 'price']
	list_search = ['name', 'slug']
	prepopulated_fields = {'slug': ('name',)}
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)