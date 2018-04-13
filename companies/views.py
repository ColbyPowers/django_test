from rest_framework import generics
from companies.models import Company, Manager, Employee
from companies.serializers import CompanySerializer, ManagerSerializer, EmployeeSerializer, EmployeeAndManagerSerializer

import ipdb

# List of all Companies


class CompanyListView(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

# List of Managers in specific company


class ManagerListView(generics.ListAPIView):
    serializer_class = ManagerSerializer

    def get_queryset(self):
        company_id = self.kwargs['company_id']
        # Having trouble applying values_list() to the query below
        return Manager.objects.filter(company_id=company_id)

# List of Employees in specific company


class EmployeeListView(generics.ListAPIView):
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        company_id = self.kwargs['company_id']
        return Employee.objects.filter(manager__company_id=company_id)

# List of Employees with their Manager in specific company


class EmployeeAndManagerListView(generics.ListAPIView):
    serializer_class = EmployeeAndManagerSerializer

    def get_queryset(self):
        company_id = self.kwargs['company_id']
        return Employee.objects.filter(manager__company_id=company_id).prefetch_related('manager')
