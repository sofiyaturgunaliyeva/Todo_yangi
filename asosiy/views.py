from django.shortcuts import render,redirect
from.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def hamma_todo(sorov):
    if sorov.method == 'POST':
        Plan.objects.create(
            sarlavha=sorov.POST.get('sarlavha'),
            batafsil=sorov.POST.get('batafsil'),
            holat=sorov.POST.get('holat'),
            vaqt=sorov.POST.get('vaqt'),
            talaba =Talaba.objects.get(user = sorov.user)
        )
        return redirect("/plans/")

    if sorov.user.is_authenticated:
        content = {
            "planlar":Plan.objects.filter(talaba = Talaba.objects.get(user = sorov.user))
        }
        return render(sorov,'index.html',content)
    return redirect("/")


def login_view(sorov):
    if sorov.method == "POST":
       user = authenticate(               # bor bo'lsa userni , yo'q bo'lsa None
            username = sorov.POST.get('l'),
            password = sorov .POST.get('p')
        )
       if user is None:
            messages.error(sorov,'Login yoki parolda xatolik bor')
            return redirect("login")
       login(sorov,user)
       return redirect("/plans/")
    return render(sorov, 'login.html')

def logout_view(sorov):
    logout(sorov)
    return redirect("/")


# Vazifa

# 2-topshiriq   Foydalanuvchi biron rejani o'chiqmoqchi bo'lsa,
# shu reja faqat o'ziga tegishli bo'lsagina o'chib ketsin.

def reja_ochir(sorov,son):
    Plan.objects.filter(foydalanuvchi = sorov.user, id = son).delete()
    return redirect('/plans/')


def register(sorov):
    if sorov.method == 'POST' and sorov.POST.get('p') == sorov.POST.get('p2'):
        u = User.objects.create_user(
            username = sorov.POST.get('l'),
            password = sorov.POST.get('p')
        )
        Talaba.objects.create(
            ism = sorov.POST.get('i'),
            yosh = sorov.POST.get('y'),
            kurs = sorov.POST.get('k'),
            user = u
        )
        return redirect('login')
    return render(sorov,'register.html')