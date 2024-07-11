from django.db import models
from django.utils.timezone import now
# Create your models here.

class patient_register(models.Model):
    First_name=models.CharField(max_length=50,default="")
    Last_name=models.CharField(max_length=50,default="")
    Email=models.CharField(max_length=30)
    Phone=models.CharField(max_length=40,default="")
    Password=models.CharField(max_length=20,default="")
    DOB=models.CharField(max_length=10,default="")
    Address=models.CharField(max_length=30,default="")
    Image=models.ImageField(upload_to='Image/',default="https://img.freepik.com/free-vector/user-circles-set_78370-4704.jpg?size=626&ext=jpg&ga=GA1.1.199161677.1717694373&semt=ais_user")
    Date_time=models.CharField(max_length=50,default=now)
    def __str__(self):
        return self.First_name
class appointment(models.Model):
    Blood_group=models.CharField(max_length=20,default="")
    Gender=models.CharField(max_length=20,default="")
    Disease=models.CharField(max_length=20,default="")
    patient_fkey=models.ForeignKey(patient_register,on_delete=models.CASCADE)
    Appointment_date=models.CharField(max_length=50,default=now())
    def __str__(self):
        return self.Blood_group

class Payment(models.Model):
    payment_id = models.CharField(max_length=100, blank=True, null=True)
    amount = models.FloatField()
    created_at = models.CharField(max_length=50,default=now())
    patient_fkey=models.ForeignKey(patient_register,on_delete=models.CASCADE)
    appointment_fkey=models.ForeignKey(appointment,on_delete=models.CASCADE)
    def __ste__(self):
        return self.payment_id

    
