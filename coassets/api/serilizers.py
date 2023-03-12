from rest_framework import serializers
from coassets.models import Company,Employee,Device



class CompanySerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Company
        fields = '__all__'


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        exclude = ('employee',)


class EmployeeSerializer(serializers.ModelSerializer):
    devices = DeviceSerializer(many=True,read_only=True)
    class Meta:
        model = Employee
        fields = '__all__'

