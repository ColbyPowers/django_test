from django.db import models


class Company(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Manager(models.Model):
    id = models.AutoField(primary_key=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    job_title = models.CharField(max_length=30, default="Manager")

    def __str__(self):
        return self.name


class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    job_title = models.CharField(max_length=30, default="Developer")

    def __str__(self):
        return self.name
