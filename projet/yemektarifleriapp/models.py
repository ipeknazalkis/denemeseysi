from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    ad = models.CharField(max_length=50)
    soyad = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    dogum_tarihi = models.DateField(null=True, blank=True)
    boy = models.FloatField(null=True, blank=True)  
    kilo = models.FloatField(null=True, blank=True)  

    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ["email", "ad", "soyad"]

    def _str_(self):
        return self.username