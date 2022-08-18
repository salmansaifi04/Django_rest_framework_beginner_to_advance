from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse


## Model Object - Single Student Data
def student_data(request, pk):
    stu = Student.objects.get(id=pk)
    serializers = StudentSerializer(stu)
    # json_data = JSONRenderer().render(serializers.data)
    # return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(serializers.data)

## QuerySet - All Student Data
def student_list(request):
    stu = Student.objects.all()
    serializer = StudentSerializer(stu, many=True)
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(serializer.data, safe=False)
