from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response

from apps.utils.custom_api_views import JWTAPIView
from apps.utils.exceptions import GeneralAPIException


class AuthenticateUserAPIView(JWTAPIView):
    def post(self, request):
        user = self.get_object()

        if not user.check_password(request.POST.get("password")):
            raise AuthenticationFailed("Usuario o contraseña inválidos")

        response = {
            "token": self.generate_token(
                user_id=user.id,
            ),
        }

        return Response(response)

    def get_object(self):
        if not "username" in self.request.POST or not "password" in self.request.POST:
            raise GeneralAPIException(
                detail={"error": "El nombre de usuario y la contraseña son requeridos"},
                code=status.HTTP_400_BAD_REQUEST,
            )
        try:
            username = self.request.POST.get("username")
            return User.objects.get(username=username)
        except User.DoesNotExist:
            raise GeneralAPIException(
                detail="Usuario no existe", code=status.HTTP_404_NOT_FOUND
            )

