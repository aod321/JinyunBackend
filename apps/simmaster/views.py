from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from apps.simmaster.models import MyUser, PlayInfo
from apps.simmaster.serializers import UserSerializer, GroupSerializer, MyUserSerializer, PlayInfoSerializer
from apps.simmaster.custom_viewset import NewModelViewSet


class UserViewSet(NewModelViewSet):
    """
    用户管理
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
        
    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return MyUser.objects.all()
        return MyUser.objects.filter(id=user.id)


class GroupViewSet(NewModelViewSet):
    """
    权限组管理
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]



class MyUserViewSet(NewModelViewSet):
    """
    用户管理
    """
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer
    permission_classes = [permissions.AllowAny]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    # def get_queryset(self):
    #     user = self.request.user
    #     if user.is_superuser:
    #         return MyUser.objects.all()
    #     return MyUser.objects.filter(user_id=user.id)

class PlayInfoViewSet(NewModelViewSet):
    """
    实验记录管理
    """
    queryset = PlayInfo.objects.all()
    serializer_class = PlayInfoSerializer
    permission_classes = [permissions.AllowAny]
    # permission_classes = [permissions.IsAuthenticated]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    # def get_queryset(self):
    #     user = self.request.user
    #     if user.is_superuser:
    #         return PlayInfoViewSet.objects.all()
    #     return PlayInfoViewSet.objects.filter(user_id=user.id)
    
