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


from django.urls import path
from .views import home, profil, ayarlar

urlpatterns = [
    path("", home, name="home"),
    path("profil/", profil, name="profil"),
    path("ayarlar/", ayarlar, name="ayarlar"),
]



from django.urls import path
from .views import home

urlpatterns = [
    path("", home, name="home"),
]
