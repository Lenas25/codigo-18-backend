from django.db import models

# Create your models here.

# RETO -> crear una clase Category con los siguientes campos:
class Category(models.Model):
  name = models.CharField(max_length=255, null=False, blank=True)
  description = models.CharField(max_length=255, null=False, blank=True)
  is_active = models.BooleanField(default=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  def __str__(self) -> str:
    return self.name
  
  class Meta:
    db_table='categories'
  

class Product(models.Model):
  name = models.CharField(max_length=255, null=False, blank=True)
  description = models.TextField(null=False, blank=True)
  price = models.FloatField(null=False, blank=True)
  stock = models.PositiveIntegerField(default=0)
  category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
  image = models.TextField(null=False, blank=True)
  is_active = models.BooleanField(default=True)
  created_at = models.DateTimeField(auto_now_add=True) 
  updated_at = models.DateTimeField(auto_now=True)
  
  # para que se muestre el nombre del producto en el admin
  def __str__(self) -> str:
    return self.name
  
  class Meta:
    db_table = 'products'
