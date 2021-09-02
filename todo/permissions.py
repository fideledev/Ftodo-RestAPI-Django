from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit there own profile"""
    def has_object_permission(self, request, view, obj):
        """Check user if he is allowed to update his own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id == request.user.id


class TaskForUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == permissions.SAFE_METHODS:
            return True
        return obj.user == request.user