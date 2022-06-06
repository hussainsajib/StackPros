from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from . import models
from . import serializers


@api_view(['GET'])
def file_structure(request, path):
    queries = path.split("/")
    if queries[0] != "root":
        raise Http404
    node = models.FileStructure.objects.get(name=queries[-1])
    children = list(models.FileStructure.objects.filter(parent=node))
    child_serializer = serializers.FileStructureSerializer(children, many=True)
    serializer = serializers.FileStructureSerializer(node)
    return Response({"current": serializer.data, "children": child_serializer.data})
