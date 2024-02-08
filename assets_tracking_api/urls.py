from django.urls import path
from . import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Device tracking api",
        default_version='v1',
        description="Django app to track corporate assets such as phones, tablets laptops and other gears handed out to employees."
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('company/', views.CompanyView.as_view(), name='company_info'),
    path('company/<int:pk>', views.CompanyDetail.as_view(), name='company_detail'),
    path('company/employees/', views.EmployeeList.as_view(), name='employee_list'),
    path('company/employees/<int:pk>/', views.EmployeeDetail.as_view(), name='employee_detail'),
    path('company/devices/', views.DeviceList.as_view(), name='device_list'),
    path('company/devices/<int:pk>/', views.DeviceDetail.as_view(), name='device_detail'),
    path('company/devices-log/', views.DeviceLogList.as_view(), name='device_log_list'),
    path('company/devices-log/<int:pk>/', views.DeviceLogDetail.as_view(), name='device_log_detail'),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]