from rest_framework import viewsets
from .models import Note
from .serializers import NoteSerializer
from rest_framework import status
from rest_framework.response import Response

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all().order_by('-created_at')
    serializer_class = NoteSerializer

    def update(self, request, *args, **kwargs):
        partial = True  # <- allow partial updates
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)