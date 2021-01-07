from django.contrib import admin
from django.urls import path,include
from .views import *

app_name = 'authentication'

urlpatterns = [    
    path('register/',RegisterUserView.as_view()),
    path('login/',LoginView.as_view()),
    path('logout/',logoutView),

   
]
