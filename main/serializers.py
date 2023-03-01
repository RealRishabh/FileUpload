from rest_framework import serializers
from .models import FileTable

class FileTableSerializer(serializers.ModelSerializer):
    class Meta():
        model = FileTable
        fields = ('file', 'created_at')