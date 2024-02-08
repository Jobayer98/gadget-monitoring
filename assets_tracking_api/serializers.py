from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Company, Device, Employee

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'
        
class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'
        
        
class EmployeeSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    company = CompanySerializer(read_only=True)
    user_id = serializers.IntegerField(write_only=True)
    company_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = Employee
        fields = ['id', 'address', 'designation', 'company', 'user', 'user_id', 'company_id']