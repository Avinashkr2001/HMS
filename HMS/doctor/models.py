from django.db import models
from django.utils.timezone import now

# Create your models here.
class doctor(models.Model):
    Name=models.CharField(max_length=20,default="")
    Doctor_id=models.CharField(max_length=50, default="")
    Specility=models.CharField(max_length=20,default="")
    Phone=models.CharField(max_length=50,default="")
    Password=models.CharField(max_length=10,default="")
    Joining_date=models.CharField(max_length=10,default=now)
    def __str__(self):
        return self.Name