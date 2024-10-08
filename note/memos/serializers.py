from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import Memo


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class MemoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Memo
        fields = ['id', 'title', 'content', 'created_at']