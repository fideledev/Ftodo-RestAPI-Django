from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class HelloAPIView(APIView):
    """Test Api view"""
    def get(self,request,format=None):
        an_apiview=[
            'Salam',
            'bimeze gt',
            'ni ndange',
            'ubufu'
        ]

        return Response({'message':'hello','apiview':an_apiview})