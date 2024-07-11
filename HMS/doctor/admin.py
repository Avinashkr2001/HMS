from django.contrib import admin
from .models import doctor


class doctorAdmin(admin.ModelAdmin):
    list_display=('Name',)
admin.site.register(doctor,doctorAdmin)
