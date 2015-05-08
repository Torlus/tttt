from django.views.generic.base import TemplateView
from django.db.models import Sum

from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import User, Group

from rest_framework.validators import ValidationError
from rest_framework import permissions, viewsets, views
# from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import Category, Project, Task, Work
from .serializers import UserSerializer, GroupSerializer
from .serializers import CategorySerializer, ProjectSerializer, TaskSerializer, WorkSerializer


class HomePageView(TemplateView):
    template_name = 'index.html'


class APIRootView(views.APIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]

    def get(self, request, format=None):
        return Response({
            'users': reverse('user-list', request=request, format=format),
            'groups': reverse('group-list', request=request, format=format),
            'categories': reverse('category-list', request=request, format=format),
            'projects': reverse('project-list', request=request, format=format),
            'tasks': reverse('task-list', request=request, format=format),
            'works': reverse('work-list', request=request, format=format),
        })


# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [
#         permissions.AllowAny
#     ]
#
#
# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [
        permissions.IsAuthenticated,
    ]


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [
        permissions.IsAuthenticated,
    ]


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [
        permissions.IsAuthenticated,
        permissions.DjangoModelPermissions,
    ]


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        permissions.DjangoModelPermissions,
    ]


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        permissions.DjangoModelPermissions
    ]

UNITS_MAX = 8


class WorkViewSet(viewsets.ModelViewSet):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        permissions.DjangoModelPermissions,
    ]

    def count_units(self):
        units = int(self.request.data['units'])
        q = Work.objects.filter(date=self.request.data['date'])
        q = q.filter(owner=self.request.data['owner'])
        total = q.aggregate(Sum('units'))['units__sum']
        if total is None:
            total = 0
        if total + units > UNITS_MAX:
            raise ValidationError('units per day must not exceed ' + str(UNITS_MAX)
                                  + ' current: ' + str(total))

    def perform_create(self, serializer):
        self.count_units()
        serializer.save(owner=self.request.user)

    def perform_update(self, serializer):
        instance = self.get_object()
        if instance.owner == self.request.user or self.request.user.is_staff:
            self.count_units()
            serializer.save()
        else:
            raise PermissionDenied
