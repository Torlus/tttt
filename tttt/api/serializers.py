from django.contrib.auth.models import User, Group
from rest_framework import serializers
from tttt.api.models import Category


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    pk = serializers.IntegerField(read_only=True)
    # url = serializers.HyperlinkedRelatedField(view_name='category-detail', read_only=True)
    code = serializers.CharField()
    title = serializers.CharField(required=False, allow_blank=True, max_length=250)

    class Meta:
        model = Category
        fields = ('pk',
                  # 'url',
                  'created_at',
                  'updated_at',
                  'code',
                  'title')
