from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm



class CustomUserRegisterForm(UserCreationForm):
    ad = forms.CharField(max_length=255, required=True, label="Ad")
    soyad = forms.CharField(max_length=255, required=True, label="Soyad")
    email = forms.EmailField(required=True, label="E-Posta")
    dogum_tarihi = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    boy = forms.DecimalField(max_digits=5, decimal_places=2)
    kilo = forms.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        model = get_user_model()
        fields = ["username", "ad", "soyad", "email", "password1", "password2", "dogum_tarihi", "boy", "kilo"]

    def clean(self):
        cleaned_data = super().clean()
        sifre = cleaned_data.get('password1')
        sifre_dogrulama = cleaned_data.get('password2')

        if sifre and sifre_dogrulama and sifre != sifre_dogrulama:
            raise forms.ValidationError('Parolalar eşleşmiyor')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        
        if commit:
            user.save()
        
        return user



# myapp/forms.py
from django import forms
from django.contrib.auth import get_user_model

class LoginForm(forms.Form):
    login = forms.CharField(max_length=255)
    sifre = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        login = cleaned_data.get('login')
        sifre = cleaned_data.get('sifre')

        try:
            user = get_user_model().objects.get(username=login)
        except get_user_model().DoesNotExist:
            try:
                user = get_user_model().objects.get(email=login)
            except get_user_model().DoesNotExist:
                raise forms.ValidationError('Kullanıcı adı veya e-posta hatalı')

        if not user.check_password(sifre):
            raise forms.ValidationError('Şifre hatalı')

        cleaned_data['user'] = user
        return cleaned_data


# myapp/forms.py
from django import forms
from django.contrib.auth import get_user_model

class ResetPasswordForm(forms.Form):
    yeni_sifre = forms.CharField(widget=forms.PasswordInput)
    sifre_dogrulama = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        yeni_sifre = cleaned_data.get('yeni_sifre')
        sifre_dogrulama = cleaned_data.get('sifre_dogrulama')        

        if yeni_sifre and sifre_dogrulama and yeni_sifre != sifre_dogrulama:
            raise forms.ValidationError('Parolalar eşleşmiyor')

        return cleaned_data






from django import forms
from django.contrib.auth.models import User
from .models import Profil, Tarif

class KayitForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')

class ProfilForm(forms.ModelForm):
    class Meta:
        model = Profil
        fields = ('foto',)

class TarifForm(forms.ModelForm):
    class Meta:
        model = Tarif
        fields = ('isim', 'icerik', 'foto', 'kategori')

class PasswordResetForm(forms.Form):
    email = forms.EmailField(max_length=255)



