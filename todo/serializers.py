from django.db.models import fields
from rest_framework import serializers
from rest_framework import permissions
from . import models
class HelloSerializer(serializers.Serializer):
    """Serializers for testing"""
    name=serializers.CharField(max_length=10)
    

class UserProfileSerializer(serializers.ModelSerializer):
    """Serializer for our user model"""

    class Meta:
        model=models.UserProfile
        fields=('id','name','email','password')
        extra_kwargs={'password':{
            'write_only':True
        }}

    def create(self,validated_data):
        """Create and return new user"""
        user=models.UserProfile(
            email=validated_data['email'],
            name=validated_data['name']
        )

        user.set_password(validated_data['password'])
        user.save()
        return user


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Task
        fields=('title','descriptions','status','user')
        extra_kwargs={'user':{
            'read_only':True,
        }}

    