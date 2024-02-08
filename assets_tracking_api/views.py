from rest_framework.response import Response
from rest_framework import generics, viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404
from .serializers import CompanySerializer, EmployeeSerializer, DeviceSerializer, DeviceLogSerializer
from .models import Company, Employee, Device, DeviceLog

@api_view()
def index(request):
    return Response("Hello world")

class CompanyView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    
    def get(self, request, *args, **kwargs):
        user_id = request.user.id
        requested_employee = get_object_or_404(Employee, id=user_id)
        company = Company.objects.get(id=requested_employee.company_id)
        serialized_item = self.serializer_class(company)
        return Response(serialized_item.data)
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    

class CompanyDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CompanySerializer
    
    def get(self, request, *args, **kwargs):
        pk = kwargs['pk']
        user = request.user
        requested_employee = get_object_or_404(Employee, id=user.id)
        company = get_object_or_404(Company, id=pk)
        if requested_employee.company_id == company.id:
            serializer = self.serializer_class(company)
            return Response(serializer.data)
        else:
            return Response({"message": "You are not authorized"}, status=status.HTTP_403_FORBIDDEN)
    
    def put(self, request, *args, **kwargs):
        pk = kwargs['pk']
        user_id = request.user.id
        requested_employee = get_object_or_404(Employee, id=user_id)
        company = get_object_or_404(Company, id=pk)
        if requested_employee.company_id == company.id:
            serializer = self.serializer_class(company, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({"message": "You are not authorized"}, status=status.HTTP_403_FORBIDDEN)
    
    def patch(self, request, *args, **kwargs):
        pk = kwargs['pk']
        user_id = request.user.id
        requested_employee = get_object_or_404(Employee, id=user_id)
        company = get_object_or_404(Company, id=pk)
        if requested_employee.company_id == company.id:
            serializer = self.serializer_class(company, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({"message": "You are not authorized"}, status=status.HTTP_403_FORBIDDEN)
    
    def delete(self, request, *args, **kwargs):
        pk = kwargs['pk']
        user_id = request.user.id
        requested_employee = get_object_or_404(Employee, id=user_id)
        company = get_object_or_404(Company, id=pk)
        if requested_employee.company_id == company.id:
            company.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"message": "You are not authorized"}, status=status.HTTP_403_FORBIDDEN)
    
    
class EmployeeList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
    def get(self, request, *args, **kwargs):
        user_id = request.user.id
        requested_employee = get_object_or_404(Employee, id=user_id)
        employees = Employee.objects.filter(company_id=requested_employee.company_id)
        serialized_item = self.serializer_class(employees, many=True)
        return Response(serialized_item.data)
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
    def get(self, request, *args, **kwargs):
        pk = kwargs['pk']
        user_id = request.user.id
        requested_employee = get_object_or_404(Employee, id=user_id)
        employee = get_object_or_404(Employee, id=pk)
        if requested_employee.company_id == employee.company_id:
            serializer = self.serializer_class(employee)
            return Response(serializer.data)
        else:
            return Response({"message": "You are not authorized"}, status=status.HTTP_403_FORBIDDEN)
    
    def put(self, request, *args, **kwargs):
        pk = kwargs['pk']
        user_id = request.user.id
        requested_employee = get_object_or_404(Employee, id=user_id)
        employee = get_object_or_404(Employee, id=pk)
        if requested_employee.company_id == employee.company_id:
            serializer = self.serializer_class(employee, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({"message": "You are not authorized"}, status=status.HTTP_403_FORBIDDEN)
        
    def patch(self, request, *args, **kwargs):
        pk = kwargs['pk']
        user_id = request.user.id
        requested_employee = get_object_or_404(Employee, id=user_id)
        employee = get_object_or_404(Employee, id=pk)
        if requested_employee.company_id == employee.company_id:
            serializer = self.serializer_class(employee, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({"message": "You are not authorized"}, status=status.HTTP_403_FORBIDDEN)
        
    def delete(self, request, *args, **kwargs):
        pk = kwargs['pk']
        user_id = request.user.id
        requested_employee = get_object_or_404(Employee, id=user_id)
        employee = get_object_or_404(Employee, id=pk)
        if requested_employee.company_id == employee.company_id:
            employee.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"message": "You are not authorized"}, status=status.HTTP_403_FORBIDDEN)
    
    
class DeviceList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    
    def get(self, request, *args, **kwargs):
        user_id = request.user.id
        requested_employee = get_object_or_404(Employee, id=user_id)
        devices = Device.objects.filter(company_id=requested_employee.company_id)
        serialized_item = self.serializer_class(devices, many=True)
        return Response(serialized_item.data)
    
    def post(self, request):
        serializer = DeviceSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class DeviceDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    
    def get(self, request, *args, **kwargs):
        pk = kwargs['pk']
        user_id = request.user.id
        requested_employee = get_object_or_404(Employee, id=user_id)
        device = get_object_or_404(Device, id=pk)
        if requested_employee.company_id == device.company_id:
            serializer = self.serializer_class(device)
            return Response(serializer.data)
        else:
            return Response({"message": "You are not authorized"}, status=status.HTTP_403_FORBIDDEN)
    
    def put(self, request, *args, **kwargs):
        pk = kwargs['pk']
        user_id = request.user.id
        requested_employee = get_object_or_404(Employee, id=user_id)
        device = get_object_or_404(Device, id=pk)
        if requested_employee.company_id == device.company_id:
            serializer = self.serializer_class(device, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({"message": "You are not authorized"}, status=status.HTTP_403_FORBIDDEN)
        
    def patch(self, request, *args, **kwargs):
        pk = kwargs['pk']
        user_id = request.user.id
        requested_employee = get_object_or_404(Employee, id=user_id)
        device = get_object_or_404(Device, id=pk)
        if requested_employee.company_id == device.company_id:
            serializer = self.serializer_class(device, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({"message": "You are not authorized"}, status=status.HTTP_403_FORBIDDEN)
        
    def delete(self, request, *args, **kwargs):
        pk = kwargs['pk']
        user_id = request.user.id
        requested_employee = get_object_or_404(Employee, id=user_id)
        device = get_object_or_404(Device, id=pk)
        if requested_employee.company_id == device.company_id:
            device.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"message": "You are not authorized"}, status=status.HTTP_403_FORBIDDEN)