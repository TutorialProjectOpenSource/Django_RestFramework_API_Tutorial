from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import  Response
from .serializers import dataSerializer
from .models import api_data
from rest_framework import status




@api_view(['POST'])   
def api_add(request):
    serializer = dataSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def api_view(request):
    data_api = api_data.objects.all()
    serializer = dataSerializer(data_api,many=True)
    return Response(serializer.data)
