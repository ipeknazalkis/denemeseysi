from django.urls import path
from .views import hosgeldin, kayit_ol

urlpatterns = [
    path("kayit/", kayit_ol, name="kayit"),
    path("hosgeldin/", hosgeldin, name = "hosgeldin"),
]



from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("password_reset/", auth_views.PasswordResetView.as_view(), name="password_reset"),
    path("password_reset/done/", auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path("reset/done/", auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
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
