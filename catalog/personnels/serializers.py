from rest_framework import serializers

from catalog.personnels.models import Personnel


class PersonnelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Personnel
        fields = ('id', 'url', 'first_name', 'last_name', 'position')
