from rest_framework import serializers

from catalog.branches.models import Branch


class BranchSerializer(serializers.HyperlinkedModelSerializer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['point'].read_only = True

        if not self.context['request'].user.has_perm('branches.change_coordinates'):
            self.fields['longitude'].read_only = True
            self.fields['latitude'].read_only = True

    class Meta:
        model = Branch
        fields = ('id', 'url', 'name', 'facade', 'latitude', 'longitude', 'point')
