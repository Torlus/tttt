from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Category, Project, Task, Work


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'url',
                  'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'url',
                  'name')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'url', 'created_at', 'updated_at',
                  'code', 'title')


class ProjectSerializer(serializers.ModelSerializer):
    category_url = serializers.HyperlinkedRelatedField(source='category', read_only=True, view_name='category-detail')

    class Meta:
        model = Project
        fields = ('id', 'url', 'created_at', 'updated_at',
                  'code', 'title',
                  'category', 'category_url')


class TaskSerializer(serializers.ModelSerializer):
    project_url = serializers.HyperlinkedRelatedField(source='project', read_only=True, view_name='project-detail')

    class Meta:
        model = Task
        fields = ('id', 'url', 'created_at', 'updated_at',
                  'code', 'title',
                  'project', 'project_url')


class WorkSerializer(serializers.ModelSerializer):
    task_url = serializers.HyperlinkedRelatedField(source='task', read_only=True, view_name='task-detail')
    date = serializers.DateField(required=True)
    units = serializers.IntegerField(required=True, min_value=1)
    owner_url = serializers.HyperlinkedRelatedField(source='owner', read_only=True, view_name='user-detail')

    class Meta:
        model = Work
        fields = ('id', 'url', 'created_at', 'updated_at',
                  'date', 'units',
                  'task', 'task_url', 'owner', 'owner_url')
