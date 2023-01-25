from rest_framework import serializers
from .models import CustomerApplication, CustomerProjectApplication


class CustomerApplicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomerApplication
        fields = [
            'id', 'full_name', 'phone_number'
        ]


class CustomerProjectApplicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomerProjectApplication
        fields = [
            'id', 'company_name', 'full_name', 'phone_number', 'project_category_id', 'description'
        ]