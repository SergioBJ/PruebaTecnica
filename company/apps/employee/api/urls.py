from django.urls import path
from apps.employee.api import views


app_name = "Employees"

urlpatterns = [
    path("list/", views.ListEmployeeView.as_view(), name="list_employee"),
    path("create/", views.RegisterEmployeeAPIView.as_view(), name="register_employee"),
    path("detail/<int:id>/", views.DetailEmployeeAPIView.as_view(), name="detail_employee"),
    path("update/<int:id>/", views.UpdateEmployeeAPIView.as_view(), name="update_employee"),
    path("delete/<int:id>/", views.DeleteEmployeeAPIView.as_view(), name="delete_employee"),
]