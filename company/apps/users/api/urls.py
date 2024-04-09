from apps.users.api import views
from django.urls import path

app_name = "Users"

urlpatterns = [
    path("authenticate/", views.AuthenticateUserAPIView.as_view(), name="login"),
]
