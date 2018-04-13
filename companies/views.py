from rest_framework import generics
from companies.models import Company, Manager, Employee
from companies.serializers import CompanySerializer, ManagerSerializer, EmployeeSerializer, EmployeeAndManagerSerializer,\
    ManagerRetrieveSerializer, EmployeeRetrieveSerializer

# List View of all Companies


class CompanyListView(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

# List View of Managers in specific company


class ManagerListView(generics.ListAPIView):
    serializer_class = ManagerSerializer

    def get_queryset(self):
        company_id = self.kwargs['company_id']
        # Having trouble applying values_list() to the query below
        return Manager.objects.filter(company_id=company_id)

# List View of Employees in specific company


class EmployeeListView(generics.ListAPIView):
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        company_id = self.kwargs['company_id']
        return Employee.objects.filter(manager__company_id=company_id)

# List View of Employees with their Manager in specific company


class EmployeeAndManagerListView(generics.ListAPIView):
    serializer_class = EmployeeAndManagerSerializer

    def get_queryset(self):
        company_id = self.kwargs['company_id']
        return Employee.objects.filter(manager__company_id=company_id).prefetch_related('manager')


# Detail View of Specific Company
class CompanyRetrieveView(generics.RetrieveAPIView):
    queryset = Company.objects.all()
    lookup_url_kwarg = 'company_id'
    lookup_field = 'id'
    serializer_class = CompanySerializer


# Detail View of Specific Manager
class ManagerRetrieveView(generics.RetrieveAPIView):
    queryset = Manager.objects.all()
    lookup_url_kwarg = 'manager_id'
    lookup_field = 'id'
    serializer_class = ManagerRetrieveSerializer


# Detail View of Specific Employee
class EmployeeRetrieveView(generics.RetrieveAPIView):
    queryset = Employee.objects.all()
    lookup_url_kwarg = 'employee_id'
    lookup_field = 'id'
    serializer_class = EmployeeRetrieveSerializer
