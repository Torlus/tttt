from django.contrib.auth.models import User, Group
from .models import Category, Project, Task, Work
from rest_framework import generics, permissions, viewsets
from .serializers import UserSerializer, GroupSerializer
from .serializers import CategorySerializer, ProjectSerializer, TaskSerializer, WorkSerializer


class UserViewSet(viewsets.GenericViewSet):
    queryset = User.objects.all()


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [
        permissions.AllowAny
    ]


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.GenericViewSet):
    queryset = Group.objects.all()


class GroupList(generics.ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [
        permissions.AllowAny
    ]


class GroupDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = GroupSerializer
