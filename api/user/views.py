from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer


@api_view(['GET', 'POST'])
def users(request, version):
    if request.method == 'GET':
        serializer = UserSerializer(User.objects.all(), many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    try

    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
