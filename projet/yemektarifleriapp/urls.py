# myapp/urls.py
from django.urls import path
from .views import (
    kayit_view, kayit_hosgeldin_view, giris_view, giris_hosgeldin_view, sifre_unuttum, sifre_sifirlama, anasayfa_view,
)

urlpatterns = [
    path('kayit/', kayit_view, name='kayit'),
    path('merhaba/<str:first_name>/<str:last_name>/', kayit_hosgeldin_view, name='kayit_hosgeldin'),

    path('giris/', giris_view, name='giris'),
    path('tekrardan_merhaba/<str:first_name>/<str:last_name>/', giris_hosgeldin_view, name='giris_hosgeldin'),

    path('sifremi-unuttum/', sifre_unuttum, name='sifre_unuttum'),
    path('sifre-sifirla/<uidb64>/<token>/', sifre_sifirlama, name='sifre_sifirlama'),
    path('sifre-sifirlama/tamam/', PasswordResetCompleteView.as_view(), name='sifre_sifirmala_tamamlandi'),
    path('', anasayfa_view, name='anasayfa'),
]
