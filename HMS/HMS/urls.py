"""
URL configuration for HMS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from .import settings
from django .conf .urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("patient.urls"),name="patient"),
    path("doctor/",include("doctor.urls"),name="doctor"),
    path("department/",include("department.urls"),name="department"),
    path("hms_admin/",include("hms_admin.urls"),name="hms_admin"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
