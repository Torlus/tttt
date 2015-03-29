from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Category, Project


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


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'url', 'created_at', 'updated_at',
                  'code', 'title')


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    category_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Project
        fields = ('id', 'url', 'created_at', 'updated_at',
                  'code', 'title',
                  'category_id', 'category')
