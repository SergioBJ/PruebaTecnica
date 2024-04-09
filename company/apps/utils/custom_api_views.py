from rest_framework.views import APIView
from apps.utils.jwt_utils import JWTUtils


class JWTAPIView(APIView):
    def __init__(self) -> None:
        self.jwt_utils = JWTUtils()

    def generate_token(
        self, user_id
    ):
        token = self.jwt_utils.generate_jwt(
            {
                "user_id": user_id,
            }
        )
        return token
