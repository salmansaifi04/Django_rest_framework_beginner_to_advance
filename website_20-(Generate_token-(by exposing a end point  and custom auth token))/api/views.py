## Token Authentication - Generate a Token :-
## 1. By Exposing a End Point

from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

