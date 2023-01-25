from rest_framework import serializers
from .models import Category, Project

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        fields = [
            'id', 'title'
        ]
        model = Category


class ProjectSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='project_category_id.title')
    
    class Meta:
        fields = [
            'id', 'title', 'link', 'image_url', 'category_name'
        ]
        model = Project