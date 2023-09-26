"""
URL configuration for exchange project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from shop import views
app_name="shop"

urlpatterns = [
    path('',views.home,name='home'),
    path('add_items/',views.add_items,name='add_items'),
    path('allproducts/<slug:s>',views.category_based_products,name='category_products'),
    path('item_details/<int:p>',views.item_details,name='item_details'),
    path('your_items/',views.your_items,name='your_items'),
    path('update_your_item/<int:p>',views.update_your_item,name='update_your_item'),
    path('remove_your_item/<int:p>',views.remove_your_item,name='remove_your_item'),

]
