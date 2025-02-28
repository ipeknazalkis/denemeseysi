from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser



class KayitFormu(UserCreationForm):
    ad = forms.CharField(max_length=50, required=True, label="Ad")
    soyad = forms.CharField(max_length=50, required=True, label="Soyad")
    email = forms.EmailField(required=True, label="E-Posta")
    dogum_tarihi = forms.DateField(
        required=False, widget=forms.DateInput(attrs={'type': 'date'}), label="Doğum Tarihi"
    )
    boy = forms.FloatField(required=False, label="Boy (cm)")
    kilo = forms.FloatField(required=False, label="Kilo (kg)")

    class Meta:
        model = CustomUser
        fields = ["username", "ad", "soyad", "email", "password1", "password2", "dogum_tarihi", "boy", "kilo"]