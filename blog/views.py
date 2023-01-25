from rest_framework import viewsets 
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import BlogCategory, Blog
from .serializers import BlogCategorySerializer, BlogListSerializer, BlogDetailSerializer
from django.db.models.functions import Now

class CustomModalViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        queryset = self.queryset
        if hasattr(self.queryset.model, 'title'):
            queryset = self.queryset.exclude(title__exact='')
        
        return queryset
    

class BlogCategoryView(CustomModalViewSet):
    queryset = BlogCategory.objects.all()
    serializer_class = BlogCategorySerializer
    pagination_class = None
    http_method_names = ['get']


class BlogView(CustomModalViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogDetailSerializer
    pagination_class = None
    http_method_names = ['get']
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['blog_category_id']

    def get_serializer_class(self):
        if self.action == "list":
            return BlogListSerializer
        return self.serializer_class
    
    def retrieve(self, request, *args, **kwargs):
        # customization here
        instance = self.get_object()
        instance.views += 1
        instance.save()
        related = self.get_queryset().filter(blog_category_id=instance.blog_category_id, published_date__lte=Now()).exclude(id=instance.id,)[:3]
        payload = {
            'blog': self.serializer_class(instance).data,
            'recommended': BlogListSerializer(related, many=True).data
        }
        return Response(payload)