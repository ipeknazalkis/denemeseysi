# myapp/urls.py
from django.urls import path
from .views import kayit_view, kayit_hosgeldin_view

urlpatterns = [
    path('kayit/', kayit_view, name='ksyit'),
    path('merhaba/<str:ad>/<str:soyad>/', kayit_hosgeldin_view, name='kayit_hosgeldin'),
]



# myapp/urls.py
from django.urls import path
from .views import girisn_view, sifre_unuttum

urlpatterns = [
    path('giris/', giris_view, name='giris'),
    path('sifremi-unuttum/', sifre_unuttum, name='sifre_unuttum'),
    # ... diğer URL'ler ...
]


# myapp/urls.py
from django.urls import path
from .views import reset_password

urlpatterns = [
    # ... diğer URL'ler ...
    path('sifre-sifirla/<uidb64>/<token>/', reset_password, name='sifre_sifirlama_dogrulaması'),
]



