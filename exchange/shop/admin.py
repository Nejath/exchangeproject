from django.contrib import admin

from shop.models import Category,Products


class Categoryadmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category,Categoryadmin)


class Productsadmin(admin.ModelAdmin):
    list_display = ['name','user','category','price','phone','created','updated']

admin.site.register(Products,Productsadmin)
