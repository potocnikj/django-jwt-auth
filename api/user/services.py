import hmac
import hashlib
import base64
import time
import json
from django.conf import settings
from .models import User
from django.core import serializers


class JwtService:
    """
    JwtService generates JWT tokens for purposes of authorization. It creates a header and injects
    token payload. finally it makes a digital signature of the token using SHA256 hashing algorithm and a secret.

    @create   : Generates a new token. Take desired payload as the input.

    @validate : Takes token as an input. Checks it's validity and responds accordingly.

    """

    def __init__(self, secret=settings.SECRET_KEY, expires=3600):
        self.__secret = secret
        self.__header = {"alg": "HS256", "typ": "JWT"}
        self.__payload = {"exp": 0, "iat": 0, "payload": {}}
        self.__expires = expires

    def create(self, data):
        self.__payload["payload"] = data
        self.__payload["iat"] = int(time.time())
        self.__payload["exp"] = int(time.time()) + self.__expires

        return self.__generate()

    def validate(self, token):
        split_token = token.split('.')
        if len(split_token) != 3:
            raise Exception('Incorrect number of token components.')

        signature = hmac.new(
            self.__secret.encode('ascii'),
            msg=(split_token[0] + '.' + split_token[1]).encode('ascii'),
            digestmod=hashlib.sha256).digest()

        return base64.b64encode(signature).decode() == split_token[2]

    def __generate(self):
        header = base64.b64encode(json.dumps(self.__header).encode('ascii'))
        payload = base64.b64encode(json.dumps(self.__payload).encode('ascii'))
        signature = hmac.new(
            self.__secret.encode('ascii'),
            msg=(header.decode() + '.' + payload.decode()).encode('ascii'),
            digestmod=hashlib.sha256).digest()

        return header.decode() + '.' + payload.decode() + '.' + base64.b64encode(signature).decode()


class UserService:
    def __init__(self):
        self.__jwt = JwtService()

    def authenticate(self, email, password):
        user = User.objects.get(email=email)

        if not user or (user.password != password):
            return None

        return self.__jwt.create(serializers.serialize('json', [user]))
