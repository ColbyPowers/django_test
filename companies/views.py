from rest_framework import generics
from companies.models import Company, Manager, Employee
from companies.serializers import CompanySerializer, ManagerSerializer, EmployeeSerializer, EmployeeAndManagerSerializer,\
    ManagerRetrieveSerializer, EmployeeRetrieveSerializer
from rest_framework.response import Response

import ipdb

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


# Destroy View of specific Company
class CompanyDestroyView(generics.DestroyAPIView):
    queryset = Company.objects.all()
    lookup_url_kwarg = 'company_id'
    lookup_field = 'id'
    serializer_class = CompanySerializer


# Destroy View of specific Manager
class ManagerDestroyView(generics.DestroyAPIView):
    queryset = Manager.objects.all()
    lookup_url_kwarg = 'manager_id'
    lookup_field = 'id'
    serializer_class = ManagerSerializer


# Destroy View of specific Employee
class EmployeeDestroyView(generics.DestroyAPIView):
    queryset = Employee.objects.all()
    lookup_url_kwarg = 'employee_id'
    lookup_field = 'id'
    serializer_class = EmployeeSerializer


# Update View of specific Company
class CompanyUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Company.objects.all()
    lookup_url_kwarg = 'company_id'
    lookup_field = 'id'
    serializer_class = CompanySerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)
        instance = self.get_object()
        temp = request.data.copy()
        temp['location'] = 'Fake Location'
        serializer = self.get_serializer(instance, data=temp, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

class ManagerUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Manager.objects.all()
    lookup_url_kwarg = 'manager_id'
    lookup_field = 'id'
    serializer_class = ManagerSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)
        instance = self.get_object()
        temp = request.data.copy()
        temp['job_title'] = 'Fake Job Title'
        serializer = self.get_serializer(instance, data=temp, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)


class EmployeeUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Employee.objects.all()
    lookup_url_kwarg = 'employee_id'
    lookup_field = 'id'
    serializer_class = EmployeeSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)
        instance = self.get_object()
        temp = request.data.copy()
        temp['job_title'] = 'Fake Job Title'
        serializer = self.get_serializer(instance, data=temp, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

        
