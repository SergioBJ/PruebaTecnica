from django.conf import settings
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.employee.models import Employee, Email


# @receiver(post_save, sender=Employee)
# def send_welcome_email(sender, instance, created, **kwargs):
#     from_email = getattr(settings, 'DEFAULT_FROM_EMAIL')
#
#     if created:
#         print("Signal triggered", created)
#         email_qs = Email.objects.filter(employee=instance)
#         if email_qs.exists():
#             email = email_qs.first().email
#             job_functions_formatted = "\n".join(instance.job_functions)
#
#             send_mail(
#                 subject='Bienvenido/a a la Empresa',
#                 message=f'Hola {instance.first_name}, bienvenido/a a la empresa. Estamos muy contentos de tenerte en nuestro equipo. Tus funciones incluyen:\n{job_functions_formatted}',
#                 from_email=from_email,
#                 recipient_list=[email],
#                 fail_silently=False,
#             )