from django.contrib.auth.models import User, Group
from rest_framework import serializers

from apps.simmaster.models import SimList
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class SimListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SimList
        fields = ('user', 'phone_number', 'sim_number', 'carrier', 'location', 'current_balance',
                  'monthly_cost', 'comments')
