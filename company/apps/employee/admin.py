from django.contrib.admin import register, ModelAdmin

from apps.employee.models import Employee, Email, Phone


# Register your models here.

@register(Employee)
class EmployeeAdmin(ModelAdmin):
    list_display = ("id", "first_name", "last_name", "position")


@register(Email)
class EmailAdmin(ModelAdmin):
    list_display = ("id", "email", "employee")


@register(Phone)
class PhoneAdmin(ModelAdmin):
    list_display = ("id", "indicative", "phone_number", "employee")
