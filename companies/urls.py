from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^company/$', views.CompanyListView.as_view(), name='company_listing'),
    url(r'^manager/(?P<company_id>[0-9a-z-]+)/$',
        views.ManagerListView.as_view(), name='manager_listing'),
    url(r'^employee/(?P<company_id>[0-9a-z-]+)/$',
        views.EmployeeListView.as_view(), name='employee_listing'),
    url(r'^employee_and_manager/(?P<company_id>[0-9a-z-]+)/$',
        views.EmployeeAndManagerListView.as_view(), name='employee_and_manager_listing'),
    url(r'^retrieve/company/(?P<company_id>[0-9a-z-]+)/$',
        views.CompanyRetrieveView.as_view(), name='company_retrieval'),
    url(r'^retrieve/manager/(?P<manager_id>[0-9a-z-]+)/$',
        views.ManagerRetrieveView.as_view(), name='manager_retrieval'),
    url(r'^retrieve/employee/(?P<employee_id>[0-9a-z-]+)/$',
        views.EmployeeRetrieveView.as_view(), name='employee_retrieval'),
]
