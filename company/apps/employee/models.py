from django.contrib.postgres.fields import ArrayField
from django.db import models


# Create your models here.

class Employee(models.Model):
    CHOICE_DOCUMENT_TYPE = [
        ("CC", "Cédula de Ciudadanía"),
        ("NIT", "Nit"),
    ]

    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    document_type = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        choices=CHOICE_DOCUMENT_TYPE
    )
    identification = models.CharField(max_length=12, null=False, blank=False)
    enter_date = models.DateField(null=False, blank=False)
    salary = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False)
    position = models.CharField(max_length=50, null=False, blank=False)
    department = models.CharField(max_length=50, null=False, blank=False)
    job_functions = ArrayField(models.CharField(max_length=100), blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Phone(models.Model):
    CHOICE_PHONE_TYPE = [
        ("cell", "Celular"),
        ("tel", "Telefono")
    ]

    phone_number = models.CharField(max_length=10, null=False, blank=False)
    indicative = models.CharField(max_length=4, null=False, blank=False)
    employee = models.ForeignKey(Employee, related_name="phone_employee", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.employee.first_name} {self.employee.last_name}"


class Email(models.Model):
    email = models.EmailField(max_length=254, null=False, blank=False, unique=True)
    employee = models.ForeignKey(Employee, related_name="email_employee", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.employee.first_name} {self.employee.last_name}"
