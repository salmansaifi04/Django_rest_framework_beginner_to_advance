import json
from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .models import Student
from .serializers import StudentSerializer
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def student_api(request):
    ## get the data
	if request.method == "GET":
		json_data = request.body
		stream = io.BytesIO(json_data)
		pythondata = JSONParser().parse(stream)
		id = pythondata.get('id', None)
		if id is not None:
			stu = Student.objects.get(id=id)
			serializer = StudentSerializer(stu)
			return JsonResponse(serializer.data, safe=True)

		student = Student.objects.all()
		serializer = StudentSerializer(student, many=True)
		return JsonResponse(serializer.data,safe=False)		

	## post the data
	if request.method == "POST":
		json_data = request.body
		stream = io.BytesIO(json_data)
		pythondata = JSONParser().parse(stream)
		serializer = StudentSerializer(data=pythondata)
		if serializer.is_valid():
			serializer.save()
			res = {'msg':'Data created'}
			json_data = JSONRenderer().render(res)
			return HttpResponse(json_data, content_type='application/json')
		json_data = JSONRenderer().render(serializer.errors)
		return HttpResponse(json_data, content_type='application/json')
	
	## update(when we update partialy then write 'partial=True')
	if request.method == 'PUT':
		json_data = request.body
		stream = io.BytesIO(json_data)
		pythondata = JSONParser().parse(stream)
		id = pythondata.get('id')
		stu = Student.objects.get(id=id)
		## patch (partially update)
		# serializer = StudentSerializer(stu, data=pythondata, partial=True)
		## put (complete update)
		serializer = StudentSerializer(stu, data=pythondata)
		if serializer.is_valid():
			serializer.save()
			res = {'msg':'Data updated'}
			json_data = JSONRenderer().render(res)
			return HttpResponse(json_data, content_type='application/json')
		json_data = JSONRenderer().render(serializer.errors)
		return HttpResponse(json_data, content_type='application/json')

	if request.method == 'DELETE':
		json_data = request.body
		stream = io.BytesIO(json_data)
		pythondata = JSONParser().parse(stream)
		id = pythondata.get('id')
		stu = Student.objects.get(id=id)
		stu.delete()
		res = {'msg':'Data deleted'}
		# json_data = JSONRenderer().render(res)
		# return HttpResponse(json_data, content_type='application/json')
		return JsonResponse(res, safe=False)