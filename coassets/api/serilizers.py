from rest_framework import serializers
from coassets.models import Company,Employee,Device



class CompanySerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Company
        exclude = ('user',)


class DeviceSerializer(serializers.ModelSerializer):
    employee = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Device
        exclude = ('check_out','returned')


class EmployeeSerializer(serializers.ModelSerializer):
    devices = DeviceSerializer(read_only=True)
    class Meta:
        model = Employee
        fields = '__all__'

