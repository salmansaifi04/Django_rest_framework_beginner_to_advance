from django.shortcuts import render
from .models import Student
from .serializer import StudentSerializer
from rest_framework.generics import ListAPIView
# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

# Create your views here.
class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    ## serach filter
    # filter_backends = [SearchFilter]
    # search_fields = ['city']
    # search_fields = ['city', 'passby']

    ## Ordering filter
    filter_backends = [OrderingFilter]
    ordering_fields = ['name']
    # ordering_fields = ['city', 'passby']
    # ordering_fields = '__all__'
