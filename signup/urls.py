# signup/urls.py
from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.get_user, name='signup'),
]
