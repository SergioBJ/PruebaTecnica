from django.conf import settings
from django.core.mail import send_mail, EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from rest_framework import generics
from rest_framework.generics import UpdateAPIView, RetrieveAPIView, DestroyAPIView

from apps.employee.api.serializers import EmployeeSerializer, ListEmployeeSerializer
from apps.employee.models import Employee, Phone, Email
from apps.utils.mixins import TokenRequiredMixin
from django.db import transaction

class ListEmployeeView(generics.ListAPIView):
    serializer_class = ListEmployeeSerializer
    queryset = Employee.objects.all()


class RegisterEmployeeAPIView(TokenRequiredMixin, generics.CreateAPIView):
    serializer_class = EmployeeSerializer

    def perform_create(self, serializer):
        with transaction.atomic():
            email_data = serializer.validated_data.pop('email', None)
            phone_number_data = serializer.validated_data.pop('phone_number', None)
            indicative_number_data = serializer.validated_data.pop('indicative_number', None)

            employee = Employee.objects.create(**serializer.validated_data)

            if phone_number_data and indicative_number_data:
                    Phone.objects.create(employee=employee, indicative=indicative_number_data, phone_number=phone_number_data)

            if email_data:
                Email.objects.create(employee=employee, email=email_data)

                html_content = render_to_string('welcome_email.html', {
                    'first_name': employee.first_name,
                    'job_functions': employee.job_functions
                })
                text_content = strip_tags(html_content)

                email = EmailMultiAlternatives(
                    subject='Bienvenido/a a la Empresa',
                    body=text_content,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    to=[email_data]
                )
                email.attach_alternative(html_content, "text/html")
                email.send()


class DetailEmployeeAPIView(TokenRequiredMixin, RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'id'


class UpdateEmployeeAPIView(TokenRequiredMixin, UpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'id'

    def perform_update(self, serializer):
        with transaction.atomic():
            instance = serializer.save()
            phone_number = serializer.validated_data.get('phone_number')
            indicative_number = serializer.validated_data.get('indicative_number')
            email = serializer.validated_data.get('email')

            if phone_number and indicative_number:
                Phone.objects.update_or_create(employee=instance,
                                               defaults={'phone_number': phone_number, 'indicative': indicative_number})

            if email:
                Email.objects.update_or_create(employee=instance, defaults={'email': email})


class DeleteEmployeeAPIView(TokenRequiredMixin, DestroyAPIView):
    queryset = Employee.objects.all()
    lookup_field = 'id'
