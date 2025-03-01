from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm



class CustomUserRegisterForm(UserCreationForm):
    ad = forms.CharField(max_length=255, required=True, label="Ad")
    soyad = forms.CharField(max_length=255, required=True, label="Soyad")
    email = forms.EmailField(required=True, label="E-Posta")
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    dogum_tarihi = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    boy = forms.DecimalField(max_digits=5, decimal_places=2)
    kilo = forms.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        model = get_user_model()
        fields = ["kullanici_adi", "ad", "soyad", "email", "sifre1", "sifre2", "dogum_tarihi", "boy", "kilo"]

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError('Parolalar eşleşmiyor')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        
        if commit:
            user.save()
        
        return user



# myapp/forms.py
from django import forms
from django.contrib.auth import get_user_model

class LoginForm(forms.Form):
    giris = forms.CharField(max_length=255)
    sifre = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        giris = cleaned_data.get('login')
        sifre = cleaned_data.get('password')

        try:
            user = get_user_model().objects.get(kullanici_adi=login)
        except get_user_model().DoesNotExist:
            try:
                user = get_user_model().objects.get(email=login)
            except get_user_model().DoesNotExist:
                raise forms.ValidationError('Kullanıcı adı veya e-posta hatalı')

        if not user.check_sifre(sifre):
            raise forms.ValidationError('Şifre hatalı')



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

        if yeni_sfire and sifre_dogrulama and yeni_sifre != sifre_dogrulama:
            raise forms.ValidationError('Parolalar eşleşmiyor')

        cleaned_data['user'] = user
        return cleaned_data

