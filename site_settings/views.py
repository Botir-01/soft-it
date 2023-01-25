from rest_framework import viewsets
from rest_framework.response import Response
from .models import Menu, CompanyInfo, AboutCompany
from portfolio.models import Project
from service.models import Service, Partner
from vacancy.models import Vacancy
from .serializers import CompanyInforSerializer, MenuSerializer, IndexAboutUsSerializer, \
                        IndexVacancySerializer, IndexPortfolioSerializer, IndexServiceSerializer, \
                        IndexPartnerSerializer, CompanyInfoFooterSerializer, MenuFooterSerializer, \
                        AboutCompanySerializer


class CustomModalViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        queryset = self.queryset
        if hasattr(self.queryset.model, 'title'):
            queryset = self.queryset.exclude(title__exact='')
        
        return queryset


class HeaderView(CustomModalViewSet):
    queryset = CompanyInfo.objects.all()
    serializer_class = MenuSerializer
    pagination_class = None
    http_method_names = ['get']


    def list(self, request, *args, **kwargs):
        company = self.get_queryset().last()
        menus = Menu.objects.filter(parent__isnull=True)
        menu_serializer = self.serializer_class
        company_serializer = CompanyInforSerializer
        payload = {
            'company_info': company_serializer(company).data,
            'menus': menu_serializer(menus, many=True).data,
        }
        return Response(payload)
    

class IndexView(CustomModalViewSet):
    queryset = AboutCompany.objects.all()
    serializer_class = IndexAboutUsSerializer
    pagination_class = None
    http_method_names = ['get']


    def list(self, request, *args, **kwargs):
        about = self.get_queryset().last()
        portfolio = Project.objects.filter(is_main=True)
        services = Service.objects.filter(is_main=True)
        partners = Partner.objects.all()
        hot_vacancies = Vacancy.objects.filter(is_main=True)
        about_serializer = self.serializer_class
        payload = {
            'about': about_serializer(about).data,
            'portfolio': IndexPortfolioSerializer(portfolio, many=True).data,
            'services': IndexServiceSerializer(services, many=True).data,
            'partners': IndexPartnerSerializer(partners, many=True).data,
            'hot_vacancies': IndexVacancySerializer(hot_vacancies, many=True).data,
        }
        return Response(payload)
    

class FooterView(CustomModalViewSet):
    queryset = CompanyInfo.objects.all()
    serializer_class = CompanyInfoFooterSerializer    
    pagination_class = None
    http_method_names = ['get']


    def list(self, request, *args, **kwargs):
        company_info = self.get_queryset().last()
        menus = Menu.objects.filter(parent__isnull=True, is_footer=True)
        company_info_serializer = self.get_serializer_class()
        menus_serializer = MenuFooterSerializer
        payload = {
            'company_info': company_info_serializer(company_info).data,
            'menus': menus_serializer(menus, many=True).data,
        }
        return Response(payload)
    

class AboutView(CustomModalViewSet):
    queryset = AboutCompany.objects.all()
    serializer_class = AboutCompanySerializer
    pagination_class = None
    http_method_names = ['get']