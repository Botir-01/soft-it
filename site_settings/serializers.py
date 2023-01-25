from rest_framework import serializers
from site_settings.models import Menu, CompanyInfo, AboutCompany, CompanyImage
from portfolio.models import Project
from service.models import Service, Partner
from vacancy.models import Vacancy

# Header
class SubMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = [
            'id', 'title', 'url'
            ]
        

class CompanyInforSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyInfo
        fields = [
            'id', 'logo_title', 'logo_description', 'logo_url', 'phone_number'
        ]


class MenuSerializer(serializers.ModelSerializer):
    child = serializers.SerializerMethodField()

    class Meta:
        model = Menu
        fields = [
            'id', 'title', 'url', 'order', 'is_footer', 'parent', 'child'
            ]


    def get_child(self, obj):
        sub_menu = Menu.objects.filter(parent=obj)
        if sub_menu.exists():
            return SubMenuSerializer(sub_menu, many=True).data
        return []
    

# Index 
class IndexCompanyImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = CompanyImage
        fields = [
            'id', 'title', 'image_url'
        ]


class IndexAboutUsSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    class Meta:
        fields = [
            'id', 'short_description', 'images'
        ]
        model = AboutCompany

    def get_images(self, obj):
        images = CompanyImage.objects.filter(company_id=obj, main=True)
        return IndexCompanyImageSerializer(images, many=True).data
    

class IndexPortfolioSerializer(serializers.ModelSerializer):
    category_title = serializers.CharField(source='project_category_id.title')

    class Meta:
        model = Project
        fields = [
            'id', 'title', 'category_title', 'link', 'image_url'
        ]


class IndexServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = [
            'id', 'title', 'description'
        ]


class IndexPartnerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Partner
        fields = [
            'id', 'title', 'link', 'image_url'
        ]


class IndexVacancySerializer(serializers.ModelSerializer):

    class Meta:
        model = Vacancy
        fields = [
            'id', 'title'
        ]


class MenuFooterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Menu
        fields = [
            'id', 'title', 'url'
            ]


class CompanyInfoFooterSerializer(serializers.ModelSerializer):

    class Meta:
        model = CompanyInfo
        fields = [
            'id', 'telegram_link', 'facebook_link', 'instagram_link', 'email', 'phone_number',
            'logo_url', 'logo_title'
        ]


class CompanyImageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CompanyImage
        fields = [
            'id', 'content', 'image_url'
        ]


class AboutCompanySerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    class Meta:
        fields = [
            'id', 'title', 'description', 'images'
        ]
        model = AboutCompany

    def get_images(self, obj):
        images = CompanyImage.objects.filter(company_id=obj, main=False)
        return CompanyImageSerializer(images, many=True).data