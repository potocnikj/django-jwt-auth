from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from .models import User
from .services import UserService, JwtService
from .serializers import UserSerializer
from rest_framework.renderers import JSONRenderer

service = UserService()
jwt = JwtService()


@api_view(['GET', 'POST'])
@renderer_classes((JSONRenderer,))
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

    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET', 'PUT', 'DELETE'])
@renderer_classes((JSONRenderer,))
def user(request, id, version):
    try:
        user = User.objects.get(user_id=id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['POST'])
@renderer_classes((JSONRenderer,))
def authenticate(request, version):
    if request.method != 'POST':
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    if not request.data['email'] and request.data['password']:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    response = dict()
    response['token'] = service.authenticate(request.data['email'], request.data['password'])

    if not response['token']:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    return Response(response)


@api_view(['GET'])
@renderer_classes((JSONRenderer,))
def authorize(request, version):
    token = request.META.get('HTTP_ACCESS_TOKEN')
    if not (token and jwt.validate(token)):
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    return Response(status=status.HTTP_200_OK)
