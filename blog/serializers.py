from rest_framework import serializers
from .models import BlogCategory, Blog

class BlogCategorySerializer(serializers.ModelSerializer):

    class Meta:
        fields = [
            'id', 'title'
        ]
        model = BlogCategory


class BlogListSerializer(serializers.ModelSerializer):

    class Meta:
        fields = [
            'id', 'title', 'short_description', 'cover_image_url', 'views', 'published_date'
        ]
        model = Blog


class BlogDetailSerializer(serializers.ModelSerializer):

    class Meta:
        fields = [
            'id', 'title', 'published_date', 'banner_image_url', 'views', 'description'
        ]
        model = Blog