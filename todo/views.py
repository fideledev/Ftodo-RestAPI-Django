from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from . import serializers
# Create your views here.

class HelloAPIView(APIView):
    """Test Api view"""

    serialiser_class=serializers.HelloSerializer

    def get(self,request,format=None):
        an_apiview=[
            'Salam',
            'bimeze gt',
            'ni ndange',
            'ubufu'
        ]

        return Response({'message':'hello','apiview':an_apiview})

    def post(self,request):
        """create hello message with serializer name"""

        serializer=serializers.HelloSerializer(data=request.data)
        if serializer.is_valid():
            name=serializer.data.get("name")
            message=f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)
    def put(self,request,pk=None):
        """Handles update"""

        return Response({'method':'put'})

    def patch(self,request,pk=None):
        """Updates of modified fields only"""
        return Response({'method':'patch'})

    def delete(self,request,pk=None):
        """Delete Objects"""
        return Response({'method':'delete'})


class HelloViewSet(viewsets.ViewSet):

    def list(self,request):
        an_apiview=[
            'Salam',
            'bimeze gt',
            'ni ndange',
            'ubufu'
        ]

        return Response({'message':'hello','apiview':an_apiview})