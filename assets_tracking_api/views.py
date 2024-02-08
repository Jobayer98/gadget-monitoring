from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from .serializers import CompanySerializer, EmployeeSerializer, DeviceSerializer, DeviceLogSerializer
from .models import Company, Employee, Device, DeviceLog

@api_view()
def index(request):
    return Response("Hello world")

class CompanyList(APIView):
    def get(self, request):
        company = Company.objects.all()
        serializer = CompanySerializer(company, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CompanySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    

class CompanyDetail(APIView):
    def get(self, request, pk):
        company = get_object_or_404(Company, pk=pk)
        serializer = CompanySerializer(company)
        return Response(serializer.data)
    
    def put(self, request, pk):
        company = get_object_or_404(Company, pk=pk)
        serializer = CompanySerializer(company, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def patch(self, request, pk):
        company = get_object_or_404(Company, pk=pk)
        serializer = CompanySerializer(company, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, pk):
        company = get_object_or_404(Company, pk=pk)
        company.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
class EmployeeList(APIView):
    def get(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)
    
    @csrf_exempt
    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class EmployeeDetail(APIView):
    def get(self, request, pk):
        employee = get_object_or_404(Employee, pk=pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)
    
    def put(self, request, pk):
        employee = get_object_or_404(Employee, pk=pk)
        serializer = EmployeeSerializer(employee, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def patch(self, request, pk):
        employee = get_object_or_404(Employee, pk=pk)
        serializer = EmployeeSerializer(employee, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, pk):
        employee = get_object_or_404(Employee, pk=pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
class DeviceList(APIView):
    def get(self, request):
        devices = Device.objects.all()
        serializer = DeviceSerializer(devices, many=True)
        return Response(serializer.data)
    
    @csrf_exempt
    def post(self, request):
        serializer = DeviceSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class DeviceDetail(APIView):
    def get(self, request, pk):
        device = get_object_or_404(Device, pk=pk)
        serializer = DeviceSerializer(device)
        return Response(serializer.data)
    
    def put(self, request, pk):
        device = get_object_or_404(Device, pk=pk)
        serializer = DeviceSerializer(device, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def patch(self, request, pk):
        device = get_object_or_404(Device, pk=pk)
        serializer = DeviceSerializer(device, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, pk):
        device = get_object_or_404(Device, pk=pk)
        device.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)