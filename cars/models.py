from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length=64)
    year = models.TextField()
    make = models.ForeignKey(User, on_delete=models.CASCADE)