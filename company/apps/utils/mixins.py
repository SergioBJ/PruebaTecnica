from django.contrib.auth.models import User

from apps.utils.jwt_utils import JWTUtils
from apps.utils.exceptions import GeneralAPIException
from rest_framework import status


class TokenRequiredMixin:
    def __init__(self) -> None:
        self.jwt_utils = JWTUtils()

    def get_profile(self, request):
        headers = request.META
        try:
            payload = self.jwt_utils.decode_jwt(
                headers.get("HTTP_AUTHORIZATION"),
            )
        except Exception:
            raise GeneralAPIException("El token enviado está corrupto", 400)

        try:
            user = User.objects.get(id=payload["user_id"])
        except User.DoesNotExist:
            raise GeneralAPIException(
                detail="El usuario no existe",
                code=status.HTTP_404_NOT_FOUND,
            )
        except Exception:
            raise GeneralAPIException("El token enviado está corrupto o expiró", 400)

        return user
