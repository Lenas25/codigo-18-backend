from django.db import models
from users.models import User

class Category(models.Model):
  title = models.CharField(max_length=255, null=False, blank=False)
  description = models.TextField(null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  class Meta:
    db_table = 'categories'
  
  def __str__(self):
    return self.title

class Task(models.Model):
  title = models.CharField(max_length=255, null=False, blank=False)
  description = models.TextField(null=True, blank=True)
  status = models.CharField(null=True, blank=True, choices=[
    ('created', 'Creado'),
    ('in_progress', 'En progreso'),
    ('finished', 'Terminado')
  ])
  color = models.CharField(max_length=50, null=True, blank=True)
  user_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
  category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  class Meta:
    db_table = 'tasks'
  
  def __str__(self):
    return self.title
