from django.db import models
from uuid import uuid4
# Create your models here.
# CREATE PRODUCTS 

class Products(models.Model):
  name= models.CharField(max_length=100)
  price= models.FloatField(max_length=100)
  score= models.FloatField(max_length=100)
  image= models.ImageField(upload_to='assests')

  def __str__(self):
    return self.name

# CREATE USERS
class Users(models.Model):
  user= models.CharField(max_length=100),
  senha= models.CharField(max_length=100),
  def __str__(self):
    return self.user