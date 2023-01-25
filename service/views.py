from rest_framework import viewsets
from .serializers import ServiceSerializer
from .models import Service

class CustomModalViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        queryset = self.queryset
        if hasattr(self.queryset.model, 'title'):
            queryset = self.queryset.exclude(title__exact='')
        
        return queryset


class ServiceView(CustomModalViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    pagination_class = None
    http_method_names = ['get']