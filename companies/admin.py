from django.contrib import admin

from .models import Company, Manager, Employee

admin.site.register(Company)
admin.site.register(Manager)
admin.site.register(Employee)