from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import *

urlpatterns = [
    path('register/',RegisterView.as_view(),name="register"),
    path('login/',login_,name="login"),
    path('logout/',LogoutView.as_view(next_page="login"),name='logout')
]