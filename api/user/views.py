
from rest_framework import generics
from .models import User
from .serializers import UserSerializer


class GetUsers(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
