from rest_framework import serializers
from .models import Note

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'title', 'content']
        extra_kwargs = {
            'title': {'required': False},
            'content': {'required': False},
        }
