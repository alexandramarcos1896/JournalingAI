from rest_framework import routers
from django.urls import path, include
from .views import NoteViewSet, UserProfileViewSet

router = routers.DefaultRouter()
router.register(r'notes', NoteViewSet)
router.register(r'user', UserProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]