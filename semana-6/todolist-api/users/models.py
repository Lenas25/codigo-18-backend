from django.db import models

# Create your models here.
class User(models.Model):
  name = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255, blank=True, null=True)
  email = models.EmailField(unique=True)
  password = models.CharField(max_length=300)
  is_superuser = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  class Meta:
    db_table = "users"
    
  def __str__(self):
    return f'{self.name} {self.lastname}'
  
  
  
