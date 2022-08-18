from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

## by default 'get request'
# @api_view()
# def hello_world(request):
#     return Response({'msg':'Hello World!!'})

## GET request
# @api_view(['GET'])
# def hello_world(request):
#     return Response({'msg':'Hello World!!'})

## POST request
# @api_view(['POST'])
# def hello_world(request):
#     if request.method == 'POST':
#         print(request.data)
#         return Response({'msg':'Post request'})

## GET and POST request
@api_view(['GET', "POST"])
def hello_world(request):
    if request.method == 'GET':
        return Response({'msg':'Get request !!!'})
    if request.method == 'POST':
        print(request.data)
        return Response({'msg':'Post request !!!', 'data':request.data})
