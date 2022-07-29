from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework import renderers
from rest_framework.response import Response
from .models import TrafficInfo
from .serializers import TrafficSerializer

class TrafficDataViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = TrafficInfo.objects.all()
    serializer_class = TrafficSerializer
    
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet)

    def perform_create(self, serializer):
        serializer.save()