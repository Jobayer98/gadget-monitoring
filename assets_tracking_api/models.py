from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.name


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    designation = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f'{self.user.first_name} {self.user.last_name}'


class Device(models.Model):
    device_name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    current_employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self) -> str:
        return self.device_name
    
class DeviceLog(models.Model):
    checked_out_time = models.DateField()
    returned_time = models.DateTimeField(null=True, blank=True)
    condition_when_handed_out = models.TextField()
    condition_when_returned = models.TextField(null=True, blank=True)
    device = models.ManyToManyField(Device)