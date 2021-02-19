from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from apps.simmaster.models import SimList
from apps.simmaster.serializers import UserSerializer, GroupSerializer, SimListSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    用户管理
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    权限组管理
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class SimViewSet(viewsets.ModelViewSet):
    """
    SIM卡管理
    """
    queryset = SimList.objects.all()
    serializer_class = SimListSerializer
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
