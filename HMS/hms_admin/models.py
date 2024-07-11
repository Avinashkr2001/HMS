from django.db import models
class admin_detail(models.Model):
    admin_username=models.CharField( max_length=50 ,default="hms_admin123")
    admin_password=models.CharField( max_length=20,default="admin123")
    
    def __str__(self):
        return self.admin_username