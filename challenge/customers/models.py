from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=256)
    credits = models.IntegerField(default=0)


class Customer(models.Model):
    full_name = models.CharField(max_length=256)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
