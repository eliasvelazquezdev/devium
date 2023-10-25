from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    """
    Custom permission to only allow the owner of an account to edit its details
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj == request.user