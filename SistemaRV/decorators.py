from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import AuthenticationFailed
import requests
import SistemaRV.settings as api_settings
class CustomJWTAuthentication(JWTAuthentication):
    def get_user(self, validated_token):
        user_id = validated_token[api_settings.SIMPLE_JWT['USER_ID_CLAIM']]

        # Here, you can call your user service to check if the user exists
        response = requests.get(f'http://localhost:8000/api/users/{user_id}')
        
        if response.status_code == 404:
            raise AuthenticationFailed(('User not found'), code='user_not_found')
        # You can return any user data you need here
        return response.json()  # Adjust based on the structure of your user service response

from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from functools import wraps

def jwt_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        auth = CustomJWTAuthentication()  # Use the custom class
        try:
            auth_result = auth.authenticate(request)
            if auth_result is None:
                return Response({'detail': 'Authentication credentials were not provided.'}, status=401)

            request.user, token = auth_result

        except (InvalidToken, TokenError) as e:
            return Response({'detail': str(e)}, status=401)

        return view_func(request, *args, **kwargs)

    return _wrapped_view
