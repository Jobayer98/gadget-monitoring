from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('company/', views.CompanyList.as_view(), name='company_list'),
    path('company/<int:pk>/', views.CompanyDetail.as_view(), name='company_detail'),
    path('company/employees/', views.EmployeeList.as_view(), name='employee_list'),
    path('company/employees/<int:pk>/', views.EmployeeDetail.as_view(), name='employee_detail'),
]