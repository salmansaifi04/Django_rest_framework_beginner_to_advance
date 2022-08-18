## Concrete api view
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


## create and list the data without pk
class CLStudent(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


## destroy, update, retrieve with pk
class DPRStudent(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
