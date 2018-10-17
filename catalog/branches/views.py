from rest_framework import viewsets

from catalog.branches.models import Branch
from catalog.branches.serializers import BranchSerializer


class BranchViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Branches to be viewed or edited.
    """
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
