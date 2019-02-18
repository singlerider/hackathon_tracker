from django.contrib.auth.models import Group
from mentor_tracker.models import (Device, ExpertiseCategory, Location,
                                   Organization, Personnel,
                                   PersonnelExpertiseCategory,
                                   PersonnelDevice,
                                   PersonnelOrganization)
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Personnel
        fields = (
            'url', 'username', 'email', 'groups',
            'expertise_categories', 'organizations', 'devices'
        )


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class ExpertiseCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ExpertiseCategory
        fields = ('url', 'category')


class PersonnelExpertiseCategorySerializer(
        serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PersonnelExpertiseCategory
        fields = ('url', 'personnel', 'expertise_category')


class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = (
            "url", "street_address", "building_number", "floor", "description")


class OrganizationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Organization
        fields = ("url", "name", "description")


class DeviceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Device
        fields = ("url", "make", "product", "version", "uuid")


class PersonnelOrganizationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PersonnelOrganization
        fields = ("url", "personnel", "organization", "role")


class PersonnelDeviceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PersonnelDevice
        fields = ("url", "personnel", "device", "tracked")
