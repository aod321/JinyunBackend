from django.contrib.auth.models import User, Group
from rest_framework import serializers

from apps.simmaster.models import MyUser, PlayInfo
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']
        # fields = '__all__'


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        # fields = '__all__'
        fields = ['url', 'name']


class MyUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MyUser
        fields = ['id', 'created', 'sex', 'birthday', 'rule']

class PlayInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PlayInfo
        fields = '__all__'
        # fields = ['id', 'created', 'log', 'user_id']
