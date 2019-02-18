from django.contrib.auth.models import Group
from mentor_tracker.models import ExpertiseCategory, Personnel
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Personnel
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class ExpertiseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ExpertiseCategory
        fields = ('url', 'category')
