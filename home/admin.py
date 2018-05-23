from django.contrib import admin

# Register your models here.
from .models import Staff

class StaffAdmin(admin.ModelAdmin):
    list_display = ('cashier_name', 'cashier_last_name', 'cashier_email', 'contact_number', 'status')


admin.site.register(Staff, StaffAdmin)
