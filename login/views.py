# Create your views here.
# login/views.py
from django.shortcuts import render, redirect
# from django.urls import reverse_lazy
from django.contrib.auth.hashers import check_password
from .forms import Login
from signup.models import Account


def login(request):
    if request.method == 'POST':
        form = Login(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                user = Account.objects.get(username=username)
                valid = check_password(password, user.password)
                if valid:
                    return render(request, 'home.html', {'user': username})
                    # success_url = reverse_lazy('home')
                    # return redirect(success_url, permanent=True)
            except Exception:
                form = Login()
                return render(request, 'login.html', {'wrong_user': True, 'form': form})

    else:
        form = Login()
        return render(request, 'login.html', {'form': form})
