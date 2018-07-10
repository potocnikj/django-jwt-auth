from rest_framework.response import Response
from api.user.services import JwtService
from rest_framework import status


class AuthorizationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.__jwt = JwtService()

    def __call__(self, request):
        token = request.META.get('HTTP_ACCESS_TOKEN')
        if not (token and self.__jwt.validate(token)):
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        return self.get_response(request)
