from django.contrib import admin
from .models import patient_register,appointment,Payment
# Register your models here.

admin.site.register(patient_register)
admin.site.register(appointment)
admin.site.register(Payment)

