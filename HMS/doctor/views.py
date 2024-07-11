from django.shortcuts import render
from django .http import HttpResponse
def doctor_login(request):
    return render(request,"doctor_login.html")