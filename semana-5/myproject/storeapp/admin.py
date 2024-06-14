from django.contrib import admin
from .models import Product, Category

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    # Permite crear un tupla con los campos que se quieren mostrar
    list_display = ('id', 'name', 'description', 'price', 'stock', 'category', 'is_active')
    list_filter = ('category', 'is_active')
    
class CategoryAdmin(admin.ModelAdmin):
    # Permite crear un tupla con los campos que se quieren mostrar
    list_display = ('id', 'name', 'description', 'is_active')
    list_filter = ('name', 'is_active')


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
