import json
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer


@api_view(['GET'])
@renderer_classes((JSONRenderer,))
def index(request):
    app = dict()
    app['service'] = 'User management service.'
    app['version'] = '1.0.0'
    app['author'] = 'Juicy Jane'

    return Response(app)
