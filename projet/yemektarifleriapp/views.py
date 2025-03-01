# myapp/views.py
from django.shortcuts import render, redirect
from .forms import CustomUserRegisterForm

def kayit_view(request):
    if request.method == 'POST':
        form = CustomUserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('kayit_hosgeldin', ad=user.ad, soyad=user.soyad)
    else:
        form = CustomUserRegisterForm()
    
    return render(request, 'kayit.html', {'form': form})

def kayit_hosgeldin_view(request, first_name, last_name):
    return render(request, 'kayit_hoshosgeldin.html', {'ad': ad, 'soyad': soyad})





# myapp/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import LoginForm

def giris_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            login(request, user)
            return redirect('giris_hosgeldin', ad=user.ad, soyad=user.soyad
    else:
        form = LoginForm()
    
    return render(request, 'giris.html', {'form': form})


# myapp/views.py
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth import get_user_model

def sifre_unuttum(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = get_user_model().objects.get(email=email)
            current_site = get_current_site(request)
            mail_subject = 'Şifre Sıfırlama'
            message = render_to_string('sifre_sifirlama_emaili.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email = email
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()
            return redirect('giris')
        except get_user_model().DoesNotExist:
            return render(request, 'sifre_unuttum.html', {'error': 'E-posta adresi bulunamadı'})
    return render(request, 'sifre_unuttum.html')





from django.shortcuts import render

def dashboard(request):
    return render(request, "dashboard.html")





from django.shortcuts import render
from .models import Tarif, Yorum, Begeni

def home(request):
    tarifler = Tarif.objects.all()
    return render(request, "home.html", {"tarifler": tarifler})



from django.shortcuts import render
from .models import Tarif

def home(request):
    query = request.GET.get("q", "")
    if query:
        tarifler = Tarif.objects.filter(isim__icontains=query)
    else:
        tarifler = Tarif.objects.all()
    
    return render(request, "home.html", {"tarifler": tarifler, "query": query})
