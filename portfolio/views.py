from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import Category, Project
from .serializers import CategorySerializer, ProjectSerializer

class CustomModalViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        queryset = self.queryset
        if hasattr(self.queryset.model, 'title'):
            queryset = self.queryset.exclude(title__exact='')
        
        return queryset


class CategoryView(CustomModalViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = None
    http_method_names = ['get']


class ProjectView(CustomModalViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    pagination_class = None
    http_method_names = ['get']
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['project_category_id']