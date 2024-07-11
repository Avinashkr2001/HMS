from django.urls import path
from .import views
urlpatterns = [
    path("",views.hms_admin,name="hms_admin"),
    path('admin_dashboard',views.admin_dashboard,name='admin_dashboard'),
    path('doctor_details',views.doctor_details,name="doctor_details"),
    path('patient_details',views.patient_details,name="patient_details"), 
    path('docor_add',views.doctor_add,name="doctor_add"),
    path('patient_add',views.patient_add,name='patient_add'),
    path('update_doctor=<int:id>',views.update_doctor,name="update_doctor"),
    path('delete_doctor=<int:id>',views.delete_doctor,name="delete_doctor"),
    path('appointment',views.appointment_deatils,name='appointment'),
    path('logout',views.logout,name='admin-logout') 
]