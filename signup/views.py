# Create your views here.
# signup/views.py
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.hashers import make_password
from .forms import SignUp
from .models import Account


def get_user(request):
    if request.method == 'POST':
        form = SignUp(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            password = form.cleaned_data['password']
            hashed_password = make_password(password)
            email = form.cleaned_data['email']
            user = Account(username=username, first_name=first_name, last_name=last_name, password=hashed_password,
                           email=email)
            user.save()
    else:
        form = SignUp()
        return render(request, 'signup.html', {'form': form})
    success_url = reverse_lazy('login')
    return redirect(success_url, permanent=True)
