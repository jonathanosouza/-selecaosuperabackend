from django.contrib import admin
from products.models import Products
# Register your models here.

class Produtos(admin.ModelAdmin):
  list_display = ('id','name','price','score','image',)
  list_display_links = ('id', 'name')
  search_fields=('name',)




admin.site.register(Products, Produtos)