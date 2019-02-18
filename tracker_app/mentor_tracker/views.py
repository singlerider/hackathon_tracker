from django.contrib.auth.models import Group
from mentor_tracker.models import (Device, ExpertiseCategory, Location,
                                   Organization, Personnel,
                                   PersonnelDevice,
                                   PersonnelExpertiseCategory,
                                   PersonnelLocationEntry,
                                   PersonnelOrganization)
from mentor_tracker.serializers import (DeviceSerializer,
                                        ExpertiseCategorySerializer,
                                        GroupSerializer, LocationSerializer,
                                        OrganizationSerializer,
                                        PersonnelDeviceSerializer,
                                        PersonnelExpertiseCategorySerializer,
                                        PersonnelLocationEntrySerializer,
                                        PersonnelOrganizationSerializer,
                                        PersonnelSerializer)
from rest_framework import viewsets


class PersonnelViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Personnel.objects.all().order_by('-date_joined')
    serializer_class = PersonnelSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class ExpertiseCategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows expertise categories to be viewed or edited.
    """
    queryset = ExpertiseCategory.objects.all()
    serializer_class = ExpertiseCategorySerializer


class PersonnelExpertiseCategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows personnel expertise categories to be viewed
    or edited.
    """
    queryset = PersonnelExpertiseCategory.objects.all()
    serializer_class = PersonnelExpertiseCategorySerializer


class LocationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows locations to be viewed
    or edited.
    """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class OrganizationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows organizations to be viewed or edited.
    """
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class DeviceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows devices to be viewed or edited.
    """
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


class PersonnelOrganizationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows personnel organizations to be viewed or edited.
    """
    queryset = PersonnelOrganization.objects.all()
    serializer_class = PersonnelOrganizationSerializer


class PersonnelDeviceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows personnel devices to be viewed or edited.
    """
    queryset = PersonnelDevice.objects.all()
    serializer_class = PersonnelDeviceSerializer


class PersonnelLocationEntryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows personnel locations over time to be viewed
    or edited.
    """
    queryset = PersonnelLocationEntry.objects.all().order_by('-timestamp')
    serializer_class = PersonnelLocationEntrySerializer
