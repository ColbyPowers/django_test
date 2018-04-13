from rest_framework import serializers
from companies.models import Company, Manager, Employee


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'name', 'location')


class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = ('id', 'name', 'job_title')


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'name', 'job_title')


class EmployeeAndManagerSerializer(serializers.ModelSerializer):
    manager = ManagerSerializer()

    class Meta:
        model = Employee
        fields = ('id', 'manager', 'name', 'job_title')

class ManagerRetrieveSerializer(serializers.ModelSerializer):
    company = CompanySerializer()

    class Meta:
        model = Manager
        fields = ('id', 'company', 'name', 'job_title')

class EmployeeRetrieveSerializer(serializers.ModelSerializer):
    manager = ManagerSerializer()

    class Meta:
        model = Employee
        fields = ('id', 'manager', 'name', 'job_title')



