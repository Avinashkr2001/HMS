from django.shortcuts import render, redirect,HttpResponse,get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages,sessions
from django.core.mail import send_mail
from django.utils.timezone import now
from .models import patient_register
from .forms import appoinment_form
from django.utils import timezone
from django.conf import settings
from .models import appointment
from .models import Payment
import random,string
import datetime

def patient_dashboard(request):
    email = request.session.get('user_email')
    if email:
        user = patient_register.objects.filter(Email=email)
        return render(request, "patient_dashboard.html",{"user":user})
    else:
        return redirect('patient_login')
    
def patient_profile(request):
    email = request.session.get('user_email')
    if email:
        user=patient_register.objects.filter(Email=email)
        return render(request, "profile.html",{"user":user})       
    else:
        return redirect('patient_login')
    
def patient_details(request):
    return render(request, "index.html")

def patient_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = patient_register.objects.filter(Email=email)
        
        
        
               
        if user:
            for i in user:
                user_password=i.Password
                if user_password==password:
                    request.session['user_email'] = email
                    return redirect('patient_profile')
                else:
                    messages.error(request,"Inavlid password")
        else:
            messages.error(request, "Invalid username")
    return render(request, "patient_login.html")

def generate_random_password(first_name):
    characters = string.ascii_letters + string.digits
    random_suffix = ''.join(random.choice(characters) for _ in range(5))
    return f"{first_name}{random_suffix}"
def patient_registration(request):
    if request.method == 'POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        dob=""
        address=""
        date_time=now()
        if patient_register.objects.filter(Email=email).exists():
                messages.error(request, "Entered Email already exists")
        else:
            try:
                password=generate_random_password(first_name)
                patient_ob=patient_register(First_name=first_name,Last_name=last_name,Email=email,Phone=phone,Password=password,DOB=dob,Address=address,Date_time=date_time)
                patient_ob.save()
                messages.success(request,'Check your Email for Password')
                subject="Welcome to smartxcode!"
                message=f"""
Hi {first_name},

Welcome to the smartxcode community! 🎉
We're excited to have you on board. Here's a quick rundown of what you can do next:
Explore: Dive into our features and discover everything we offer.

Your password is 👉 :{password}
Connect: Join our community forums, follow us on social media, and start connecting with other members.
Learn: Check out our tutorials, FAQs, and support center to get the most out of your experience.
If you have any questions or need assistance, feel free to reach out to our support team at website or visit our help center.

We're here to help you every step of the way. Once again, welcome to smartxcode!

Best regards,
The smartxcode Team
                    """
                email_from = 'smartxcodeotp@gmail.com'
                recipient_list = [email]
                send_mail(subject, message, email_from, recipient_list,fail_silently=False)
                return redirect('patient_login')
            except Exception as e:
                    messages.error(request, f"Error creating user:")
    return render(request, "patient_registration.html")
def generate_otp(length=6):
    otp = ''.join(random.choices('0123456789', k=length))
    return str(otp)
def forgot_pass(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:    
            if patient_register.objects.filter(Email=email).exists():
                otp = generate_otp()
                request.session['otp'] = otp
                request.session['otp_expiry'] = (timezone.now() + datetime.timedelta(minutes=2)).isoformat()
                request.session['email']=email
                subject = 'Your OTP for Password Reset'
                message = f"""We received a request to reset the password for your account associated with this email address.To proceed with resetting your password, please use the following One-Time Password (OTP):

                OTP:{otp}

                This OTP is valid for the next 2 minute. If you did not request a password reset, please ignore this email and your password will remain unchanged.

                If you have any questions or need further assistance, please contact our support team.
                Thank you,
                """
                email_from = 'smartxcodeotp@gmail.com'
                recipient_list = [email] 
                send_mail(subject, message, email_from, recipient_list, fail_silently=False)
                return redirect('email_otp')
            else:
                messages.error(request, "Please enter a valid email address")
        except Exception as e:
            messages.error(request, f"Error while processing: {e}")
    return render(request, 'forgot_pass.html')
def email_otp(request):
    if request.method == 'POST':
        entered_otp = request.POST.get('otp')
        stored_otp = request.session.get('otp')
        otp_expiry = request.session.get('otp_expiry') 
        if otp_expiry:
            otp_expiry = datetime.datetime.fromisoformat(otp_expiry)
            if otp_expiry and timezone.now() > otp_expiry:
                request.session.pop('otp',None)
                request.session.pop('otp_expiry', None)
                return
            else:
                if (entered_otp == stored_otp):
                    request.session.pop('otp',None)
                    request.session.pop('otp_expiry',None)
                    messages.success(request, "OTP verified")
                    return redirect('confirm_pass')
                else:
                    messages.error(request, "Invalid OTP. Please try again")  
                    return redirect('email_otp')
    return render(request,'email_otp.html')
def confirm_pass(request):
    if request.method=='POST':
        new_password=request.POST.get('new_password')
        confirm_password=request.POST.get('confirm_password')
        if new_password==confirm_password:
            email=request.session.get('email')
            user = patient_register.objects.get(Email=email)
            user.Password=new_password
            user.save()
            messages.success(request, "Password reset successfully")
            return redirect('patient_login')
    return render(request,'confirm_pass.html')
def profile_update(request,id):
    data = patient_register.objects.filter(id=id)
    if request.method=="POST":
        first_name=request.POST.get('first-name')
        last_name=request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        dob=request.POST.get('dob')
        address=request.POST.get('address')
        try:
            patient_ob=patient_register(First_name=first_name,Last_name=last_name,Email=email,Phone=phone,DOB=dob,Address=address)
            patient_ob.save()
            messages.success(request,'updated successfully')
            return redirect('patient_dashboard')
        except Exception as e:
            messages.error(request,'something went wrong')
    return render(request,"profile_update.html",{'user':data})

def patient_form(request):
    email = request.session.get('user_email')
    user=patient_register.objects.filter(Email=email)
    user1 = get_object_or_404(patient_register, Email=email)
    for i in user:
        id=i.id
        request.session['id'] = id
    if request.method == 'POST':
        form=appoinment_form(request.POST)
        if form.is_valid():
            blood_group=form.cleaned_data.get('Blood_group')
            gender=form.cleaned_data.get('Gender')
            disease=form.cleaned_data.get('Disease')
            appointment.objects.create(Blood_group=blood_group,Gender=gender,Disease=disease,patient_fkey=user1)
            return redirect('print_receipt')
    else:
        form=appoinment_form()
    return render(request,'patient_appointment.html',{'form':form,'user':user})
def pay_fee(request):
    id=request.session.get['id']
    amount=50000
    currency='INR'
    
    
    context={
        'amount':amount,
    }
def print_receipt(request):
    email=request.session.get('user_email')
    if email:
        user=patient_register.objects.filter(Email=email)
        user1 = get_object_or_404(patient_register, Email=email)
        data=appointment.objects.filter(patient_fkey=user1)
        return render(request,'print_receipt.html',{'user':user,'data':data})
    else:
        return redirect('patient_login')
def patient_logout(request):
    del request.session['user_email']
    del request.session['id']
    return redirect('/')
    