from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Company, Device, Employee, DeviceLog

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'
        
        
class EmployeeSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    company = CompanySerializer(read_only=True)
    class Meta:
        model = Employee
        fields = ['id', 'username', 'password', 'address', 'designation', 'company', 'user']
        

class DeviceSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)
    current_employee = EmployeeSerializer(read_only=True)
    employee_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = Device
        fields = ['id', 'device_name', 'company', 'current_employee', 'employee_id']
        
        
class DeviceLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceLog
        fields = '__all__'
