from rest_framework import viewsets 
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from .models import Vacancy, UserResume
from .serializers import VacancyDetailSerializer, VacancyListSerializer, AvailableVacancyList, \
                        UserResumeSerializer

class CustomModalViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        queryset = self.queryset
        if hasattr(self.queryset.model, 'title'):
            queryset = self.queryset.exclude(title__exact='')
        
        return queryset
    

class VacancyView(CustomModalViewSet):
    queryset = Vacancy.objects.all()
    serializer_class = VacancyDetailSerializer
    pagination_class = None
    http_method_names = ['get']

    def get_serializer_class(self):
        if self.action == "list":
            return VacancyListSerializer
        return self.serializer_class
    
    @action(detail=False, methods=['get'])
    def available_vacancies(self, request, pk=None):
        queryset = Vacancy.objects.all()
        data = AvailableVacancyList(queryset, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)


class UserResumeView(viewsets.ViewSet, CustomModalViewSet, generics.CreateAPIView):
    queryset = UserResume.objects.all()
    pagination_class = None
    http_method_names = ['post']
    serializer_class = UserResumeSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer_class()
        serializer = serializer(data=request.data)
        if serializer.is_valid():
            obj = UserResume.objects.create(**serializer.validated_data)
        
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)