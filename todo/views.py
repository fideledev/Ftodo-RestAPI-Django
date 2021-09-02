from django.http import response
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from . import serializers
from . import models
from . import permissions
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

    serializer=serializers.HelloSerializer

    def list(self,request):
        an_apiview=[
            'Salam',
            'bimeze gt',
            'ni ndange',
            'ubufu'
        ]

        return Response({'message':'hello','apiview':an_apiview})

    def create(self,request):
        serializer=serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name=serializer.data.get('name')

            message=f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    
    def retrieve(self,request,pk=None):
        """Handles for getting objects by it's Id """

        return Response({'http_method':'GET'})

    def update(self,request,pk=None):
        """Handles for updating objects by it's Id """

        return Response({'http_method':'PUT'})

    def partial_update(self,request,pk=None):
        """Handles for updating only the specific changed part by it's Id """

        return Response({'http_method':'PATCH'})

    def destroy(self,request,pk=None):
        """Delete specific object by it's id """
        return Response({'http_method':'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating,deleting and updating of profiles"""
    serializer_class=serializers.UserProfileSerializer
    queryset=models.UserProfile.object.all()

    authentication_classes=(TokenAuthentication,) # generate temporary tokens
    permission_classes=(permissions.UpdateOwnProfile,) # controll updating permission
    filter_backends=(filters.SearchFilter,) #Search feature
    search_fields=('name','email',) #search filters


class LoginViewSet(viewsets.ViewSet):
    """check email and password and return auth token"""
    serializer_class=AuthTokenSerializer

    def create(self,request):
        """user ObtainauthToken to check and obtain token"""
        return ObtainAuthToken().as_view()(request=request._request)


class TaskViewset(viewsets.ModelViewSet):
    serializer_class=serializers.TaskSerializer
    queryset=models.Task.objects.all()
    authentication_classes=(TokenAuthentication,)
    filter_backends=(filters.SearchFilter,)
    permission_classes=(permissions.TaskForUser,)
    search_fields=('title','descriptions',)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    