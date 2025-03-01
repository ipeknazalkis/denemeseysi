# myapp/views.py
from django.shortcuts import render, redirect
from .forms import CustomUserRegisterForm

def register_view(request):
    if request.method == 'POST':
        form = CustomUserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('greeting', ad=user.ad, soyad=user.soyad)
    else:
        form = CustomUserRegisterForm()
    
    return render(request, 'register.html', {'form': form})

def greeting_view(request, first_name, last_name):
    return render(request, 'greeting.html', {'first_name': first_name, 'last_name': last_name})




def hosgeldin(request):
    return render(request, "hesaplar/hosgeldin.html", {"kullanici": request.user})






from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("dashboard")  # Kullanıcı giriş yaptıktan sonra yönlendirilecek sayfa
        else:
            messages.error(request, "Kullanıcı adı veya şifre hatalı!")
    return render(request, "login.html")






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
