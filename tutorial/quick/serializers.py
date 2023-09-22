from django.contrib.auth.models import User, Group   # User, Group model from django auth
from rest_framework import serializers    #this is a serializer module from rest_framework 

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']