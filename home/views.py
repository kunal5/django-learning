from django.shortcuts import render
from login.forms import Login
from . import forms
# # Create your views here.
#
# def homepage(request):
#     if request.method == 'GET':
#         form = Home()
#         return render(request, 'home.html', {'fo'})


def homepage(request):
    if request.session.is_empty():
        form = Login()
        return render(request, 'home.html', {'form': form})
    else:
        users = list(request.session.keys())
        user = users[0]
        form = forms.Home()
        return render(request, 'home.html', {'user': user, 'form': form})

