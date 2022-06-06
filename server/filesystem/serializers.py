from rest_framework import serializers

from . import models


class FileTypesSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.FileTypes
        fields = '__all__'


class FileStructureSerializer(serializers.ModelSerializer):
    file_type = FileTypesSerializer()
    parent = serializers.StringRelatedField()

    class Meta:
        model = models.FileStructure
        fields = '__all__'

    def get_fields(self):
        fields = super(FileStructureSerializer, self).get_fields()
        fields['parent'] = FileStructureSerializer()
        return fields
