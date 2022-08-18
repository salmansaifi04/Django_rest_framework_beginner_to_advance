from django.shortcuts import render
from .models import Student
from .serializer import StudentSerializer
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.
class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['name']
    # filterset_fields = ['name', 'city']
    filterset_fields = ['name', 'passby']

    ## custom
    # def get_queryset(self):
    #     user = self.request.user
    #     return Student.objects.filter(passby=user)