from django.db import models
from django import forms

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    registration_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name  

class Product(models.Model):

  name = models.CharField(max_length=100)
  description = models.TextField()
  price = models.DecimalField(max_digits=10, decimal_places=2)
  quantity = models.PositiveIntegerField()
  added_at = models.DateTimeField(auto_now_add=True)

  image = models.ImageField(upload_to='products_images/', default='default.jpg')
  
  def __str__(self):
    return self.name


class ProductForm(forms.ModelForm):

  class Meta:
    model = Product
    fields = ['name', 'description', 'price', 'image']


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=10, decimal_places=2) 
    created_at = models.DateTimeField(auto_now_add=True)

from .models import Product