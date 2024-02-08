from django.contrib import admin
from .models import Employee, Company, Device, DeviceLog

admin.site.register(Employee)
admin.site.register(Company)
admin.site.register(Device)
admin.site.register(DeviceLog)