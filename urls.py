from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.spisok_obyavleniy, name='spisok'),  # ваш основной путь
]
from django.shortcuts import render

def signup(request):
    return render(request, 'signup.html')
