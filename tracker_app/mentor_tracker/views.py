from django.contrib.auth.models import Group
from mentor_tracker.models import ExpertiseCategory, Personnel
from mentor_tracker.serializers import (ExpertiseSerializer, GroupSerializer,
                                        UserSerializer)
from rest_framework import viewsets


class PersonnelViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Personnel.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class ExpertiseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows expertise catagories to be viewed or edited.
    """
    queryset = ExpertiseCategory.objects.all()
    serializer_class = ExpertiseSerializer
