from django.shortcuts import redirect,render
from django.urls import path
from .import views

urlpatterns = [
    path("",views.patient_details),
    path("patient_login",views.patient_login,name='patient_login'),
    path("patient_registration",views.patient_registration,name='patient_registration'),
    path('patient_dashboard',views.patient_dashboard,name='patient_dashboard'),
    path('patient_profile',views.patient_profile,name='patient_profile'),
    path('forgot_pass',views.forgot_pass,name='forgot_pass'),
    path("email_otp",views.email_otp,name='email_otp'),
    path('confirm_pass',views.confirm_pass,name='confirm_pass'),
    path('profile_update=<int:id>',views.profile_update,name='profile_update'),
    path('patient_form',views.patient_form),
    path('print_receipt',views.print_receipt,name='print_receipt'),
    path('patient_logout',views.patient_logout,name='logout'),
    # !path('patient_delete/<int:id>',views.patient_delete,name="patient_delete"),
]