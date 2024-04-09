from rest_framework import serializers

from apps.employee.models import Employee, Phone, Email


class EmployeeSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(write_only=True)
    indicative_number = serializers.CharField(write_only=True)
    email = serializers.CharField(write_only=True)

    class Meta:
        model = Employee
        fields = (
            "id", "first_name", "last_name", "email", "phone_number", "indicative_number", "document_type",
            "identification", "enter_date", "salary", "position", "department", "job_functions"
        )


class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = '__all__'


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = '__all__'


class ListEmployeeSerializer(serializers.ModelSerializer):
    phone = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()

    class Meta:
        model = Employee
        fields = (
            "id", "first_name", "last_name", "email", "phone", "document_type",
            "identification", "enter_date", "salary", "position", "department", "job_functions"
        )

    def get_phone(self, obj):
        phone = obj.phone_employee.first()
        return PhoneSerializer(phone).data if phone else None

    def get_email(self, obj):
        email = obj.email_employee.first()
        return EmailSerializer(email).data if email else None
