from rest_framework import viewsets

from catalog.personnels.models import Personnel
from catalog.personnels.serializers import PersonnelSerializer


class PersonnelViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Personnels to be viewed or edited.
    """
    queryset = Personnel.objects.all().order_by('-date_joined')
    serializer_class = PersonnelSerializer
