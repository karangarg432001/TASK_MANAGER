from rest_framework import permissions

class AdminPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_staff

class RegularUserPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Admin users have full permissions
        if request.user.is_staff:
            return True
        
        # Regular users can only view, update, and delete their own tasks
        return obj.user == request.user