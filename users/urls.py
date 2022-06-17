from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from users import views

urlpatterns = [
    path('login/', views.loginfun, name='login'),
    path('logout/', views.logoutfun, name='logout'),
    path('registration/', views.registration, name='registration')
]