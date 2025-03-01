from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    dogum_tarihi = models.DateField(null=True, blank=True)
    boy = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True) 
    kilo = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  

    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.username})"





from django.db import models
from django.contrib.auth.models import User

class Profil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='profil_fotolari', blank=True, null=True)

class Kategori(models.Model):
    isim = models.CharField(max_length=100)

    def __str__(self):
        return self.isim

class Tarif(models.Model):
    isim = models.CharField(max_length=200)
    icerik = models.TextField()
    foto = models.ImageField(upload_to='tarif_fotolari', blank=True, null=True)
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)
    begeni_sayisi = models.IntegerField(default=0)
    yorum_sayisi = models.IntegerField(default=0)

    def __str__(self):
        return self.isim
