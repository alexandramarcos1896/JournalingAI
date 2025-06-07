from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to view or edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Object-level permission: only allow the owner to access/edit it
        return obj.user == request.user