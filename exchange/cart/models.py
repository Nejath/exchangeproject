from django.db import models
from shop.models import Products
from django.contrib.auth.models import User

class Liked(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    products = models.ForeignKey(Products, on_delete=models.CASCADE)
    date_added=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.products.name