from django.shortcuts import redirect,render
from django.urls import path
from .import views

urlpatterns = [
    path("",views.doctor_login,name="doctor_login"),
]
