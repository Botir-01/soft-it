from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework import status
from .models import CustomerApplication, CustomerProjectApplication
from .serializers import CustomerApplicationSerializer, CustomerProjectApplicationSerializer


class CustomModalViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        queryset = self.queryset
        if hasattr(self.queryset.model, 'title'):
            queryset = self.queryset.exclude(title__exact='')
        
        return queryset
    

class CustomerApplicationView(viewsets.ViewSet, CustomModalViewSet, generics.CreateAPIView):
    queryset = CustomerApplication.objects.all()
    pagination_class = None
    http_method_names = ['post']
    serializer_class = CustomerApplicationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer_class()
        serializer = serializer(data=request.data)
        if serializer.is_valid():
            obj = CustomerApplication.objects.create(**serializer.validated_data)
        
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class CustomerProjectApplicationView(viewsets.ViewSet, CustomModalViewSet, generics.CreateAPIView):
    queryset = CustomerProjectApplication.objects.all()
    pagination_class = None
    http_method_names = ['post']
    serializer_class = CustomerProjectApplicationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer_class()
        serializer = serializer(data=request.data)
        if serializer.is_valid():
            obj = CustomerProjectApplication.objects.create(**serializer.validated_data)
        
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)