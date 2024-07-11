from django.contrib import admin
from .models import admin_detail

class adminAdmin(admin.ModelAdmin):
    list_display = ('admin_username',)
admin.site.register(admin_detail,adminAdmin)
