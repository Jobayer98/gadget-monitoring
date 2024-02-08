from django.urls import path
from . import views

urlpatterns = [
    path('company/', views.CompanyView.as_view(), name='company_info'),
    path('company/<int:pk>', views.CompanyDetail.as_view(), name='company_detail'),
    path('company/employees/', views.EmployeeList.as_view(), name='employee_list'),
    path('company/employees/<int:pk>/', views.EmployeeDetail.as_view(), name='employee_detail'),
    path('company/devices/', views.DeviceList.as_view(), name='device_list'),
    path('company/devices/<int:pk>/', views.DeviceDetail.as_view(), name='device_detail'),
    path('company/devices-log/', views.DeviceLogList.as_view(), name='device_log_list'),
    path('company/devices-log/<int:pk>/', views.DeviceLogDetail.as_view(), name='device_log_detail'),
]