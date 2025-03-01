from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    ad = models.CharField(max_length=255)
    soyad = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    dogum_tarihi = models.DateField(null=True, blank=True)
    boy = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True) 
    kilo = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  

    USERNAME_FIELD = "kullanici.adi"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ["email", "ad", "soyad"]

    def _str_(self):
        return self.kullanici.adi

    def __str__(self):
        return f"{self.ad} {self.soyad} ({self.kullanici_adi})"
