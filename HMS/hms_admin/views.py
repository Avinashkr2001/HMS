from django.shortcuts import render,redirect
from django.contrib import messages,sessions
from patient .models import patient_register,appointment
from django.contrib.auth import logout
from django.utils.timezone import now
from doctor .models import doctor
from .models import admin_detail
from django.urls import reverse

def hms_admin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = admin_detail.objects.filter(admin_username=username)
        if user:
            for i in user:
                if i.admin_password==password:
                    request.session['username']=username
                    return redirect('admin_dashboard')
                else:
                    messages.error(request,"Inavlid Password")
        else:
            messages.error(request,"Invalid Username")
    return render(request,"hms_admin.html")
def admin_dashboard(request):
    username = request.session.get('username')
    if username:
        return render(request,"hms_dashboard.html")
    else:
        return redirect('hms_admin')
def patient_details(request):
    username = request.session.get('username')
    if username:
        patients=patient_register.objects.all()
        return render(request,"patient_detail.html",{'patients':patients})
    else:
        return redirect('hms_admin')
def doctor_details(request):
    username = request.session.get('username')
    if username:
        doctors=doctor.objects.all()
        return render(request,"doctor_details.html",{'doctors':doctors})
    else:
        return redirect(reverse('hms_admin'))
def doctor_add(request):
    if request.method=='POST':
        id=request.POST.get('doctor-id')
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        specility=request.POST.get('specility')
        password=request.POST.get('password')
        date=now()
        if doctor.objects.filter(Doctor_id=id).exists():
            messages.error(request,'Doctor already exists')
        else:
            doctor.objects.create(Doctor_id=id,Name=name,Phone=phone,Specility=specility,Password=password,Joining_date=date)
            return redirect('doctor_details')
    return render(request,'doctor_add.html')
def update_doctor(request,id):
    details=doctor.objects.filter(id=id)
    if request.method=='POST':
        doctor_id=request.POST.get('doctor-id')
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        specility=request.POST.get('specility')
        password=request.POST.get('password')
        doctor_details=doctor(id=id,Doctor_id=doctor_id,Name=name,Phone=phone,Specility=specility,Password=password)
        doctor_details.save()
        return redirect(reverse('doctor_details'))
    return render(request,'update_doctor.html',{'details':details})
def delete_doctor(request,id):
    doctor.objects.filter(id=id).delete()
    return redirect('doctor_details')
def patient_add(request):
    return render(request,'patient_add.html')
def appointment_deatils(request):
    username = request.session.get('username')
    if username:
        appointments=appointment.objects.all()
        return render(request,"appointments.html",{'appointments':appointments})
    else:
        return redirect('hms_admin')
def logout(request):
    del request.session['username']
    return redirect('hms_admin')