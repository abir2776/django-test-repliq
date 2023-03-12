from .views import (CompanyListAv,CompanyDetailAV,
                    EmployeeListAv,EmployeeDetailAV,
                    DeviceListAv,DeviceDetailAV)
from django.urls import path,include

urlpatterns = [
    path('list/',CompanyListAv.as_view(),name='company_list'),
    path('detail/<int:pk>/',CompanyDetailAV.as_view(),name='company_detail'),
    path('employee/list/',EmployeeListAv.as_view(),name='employee_list'),
    path('employee/detail/<int:pk>/',EmployeeDetailAV.as_view(),name='employee_detail'),
    path('device/list/',DeviceListAv.as_view(),name='device_list'),
    path('device/detail/<int:pk>/',DeviceDetailAV.as_view(),name='device_detail'),
]
