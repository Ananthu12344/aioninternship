from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    Title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images')
    User = models.ForeignKey(User, on_delete=models.CASCADE)

# class Delete(models.Model):
#     Title = models.CharField(max_length=50)
#     image = models.ImageField(upload_to='images')
#     User = models.ForeignKey(User, on_delete=models.CASCADE)

# class List(models.Model):
#     Title = models.CharField(max_length=50)
#     image = models.ImageField(upload_to='images')
#     User = models.ForeignKey(User, on_delete=models.CASCADE)

# class Reterieve(models.Model):
#     Title = models.CharField(max_length=50)
#     image = models.ImageField(upload_to='images')
#     User = models.ForeignKey(User, on_delete=models.CASCADE)