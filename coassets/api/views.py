from rest_framework.response import Response
from .serilizers import CompanySerializer,EmployeeSerializer,DeviceSerializer
from coassets.models import Company,Employee,Device
from rest_framework import status
from rest_framework.views import APIView

#To show all company list and add new company
class CompanyListAv(APIView):
    def get(self,request):
        companies = Company.objects.all()
        serializer = CompanySerializer(companies,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#To get single Company details and update and delete a company
class CompanyDetailAV(APIView):
    def get(self,request,pk):
        company = Company.objects.get(pk=pk)
        serializer = CompanySerializer(company)
        return Response(serializer.data)
    def delete(self,request,pk):
        company = Company.objects.get(pk=pk) 
        company.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    def put(self,request,pk):
        company=Company.objects.get(pk=pk)
        serializer = CompanySerializer(company,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.Http_400_BAD_REQUEST)
        
#To show all Employee list and add new Employee
class EmployeeListAv(APIView):
    def get(self,request):
        emplyees = Employee.objects.all()
        serializer = EmployeeSerializer(emplyees,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#To get single Employee details and update and delete an employee
class EmployeeDetailAV(APIView):
    def get(self,request,pk):
        employee = Employee.objects.get(pk=pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)
    def delete(self,request,pk):
        employee = Employee.objects.get(pk=pk) 
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    def put(self,request,pk):
        employee=Employee.objects.get(pk=pk)
        serializer = EmployeeSerializer(employee,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.Http_400_BAD_REQUEST)
        
#To show all Device list and add new Device
class DeviceListAv(APIView):
    def get(self,request):
        devices = Device.objects.all()
        serializer = DeviceSerializer(devices,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = DeviceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#To get single Device details and update and delete a device
class DeviceDetailAV(APIView):
    def get(self,request,pk):
        device = Device.objects.get(pk=pk)
        serializer = EmployeeSerializer(device)
        return Response(serializer.data)
    def delete(self,request,pk):
        device = Device.objects.get(pk=pk) 
        device.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    def put(self,request,pk):
        device=Device.objects.get(pk=pk)
        serializer = DeviceSerializer(Device,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.Http_400_BAD_REQUEST)
